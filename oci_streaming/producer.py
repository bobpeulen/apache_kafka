from kafka3 import KafkaConsumer, KafkaProducer


#get arguments
parser = argparse.ArgumentParser()

parser.add_argument("-tenancy_name", "--tenancy_name", help="tenancy_name", required=True)
parser.add_argument("-region", "--region", help="region",required=True)
parser.add_argument("-user_name", "--user_name", help="user_name including OracleIdentityCloudService", required=True)
parser.add_argument("-stream_name", "--stream_name", help="stream_name / topic", required=True)
parser.add_argument("-stream_pool_ocid", "--stream_pool_ocid", help="stream_pool_ocid", required=True)
parser.add_argument("-auth_token", "--auth_token", help="auth_token", required=True)
parser.add_argument("-batch_size", "--batch_size", help="Set the batch size. Number of rows you want to produce and publish for each publish", required=True)
parser.add_argument("-batch_interval", "--batch_interval", help="set the batch interval. Number of seconds you want the loop to wait untill next publish.", required=True)
parser.add_argument("-max_number_of_rows", "--max_number_of_rows", help="set the maximum number of rows you want to publish", required=True)


args = parser.parse_args()
tenancy_name = args.tenancy_name
region = args.region
user_name = args.user_name
stream_name = args.stream_name
stream_pool_ocid = args.stream_pool_ocid
auth_token = args.auth_token
batch_size = args.batch_size
batch_interval = args.batch_interval
max_number_of_rows = args.max_number_of_rows


def main():
  ## create connection
  producer = KafkaProducer(bootstrap_servers = f'cell-1.streaming.{region}.oci.oraclecloud.com:9092', linger_ms = 50, batch_size  = batch_size,
                         security_protocol = 'SASL_SSL', sasl_mechanism = 'PLAIN',
                         value_serializer = lambda v: v.encode('utf-8'),
                         sasl_plain_username = f'{tenancy_name}/{user_name}/{stream_pool_ocid}',
                         sasl_plain_password = auth_token)
  #create random data
  pd_list = []

    for i in range(60):

        #set randomness, so each goes up and down together
        randomness_sun_price = random.uniform(0.95, 1.015)
        randomness_wspd = random.uniform(0.90, 0.95)
        cust_id = fake.uuid4()
        kwh_producing = round(random.uniform(0.11, 5.55), 2)
        kwh_consuming = round(random.uniform(3.55, 19.55), 2)

        ##weather info 
        temp = randomness_sun_price
        wspd =  randomness_wspd
        tsun = randomness_sun_price *1.22 
        energy_price = randomness_sun_price *0.89

        pd_list.append([cust_id, kwh_producing, kwh_consuming, temp, wspd, tsun, energy_price])
                     
    df_out = pd.DataFrame(pd_list, columns = ["cust_id", "kwh_producing", "kwh_consuming", "temp", "windspeed","sun_light", "energy_price"])

  #push random data to stream
    for index, row in df_out.iterrows():
        row_json = row.to_json(orient='records', lines=True)
        producer.send(stream_name, value=row_json)
        producer.flush()
        print(row_json)
        sleep(batch_interval)


if __name__ == '__main__':
    main()
