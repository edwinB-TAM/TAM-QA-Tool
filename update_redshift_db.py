#install these
# import psycopg2
# import yaml
from change_log_parser import *

def update_redshift_db():
    #refresh data from ironsrc kc
    data = changelogparser().get_change_logs()
    row_data = []
    for index,row in pd.DataFrame(data).iterrows():
        row_data.append("('{mediation_sdk_version}','{ad_network}','{adapter_version}','{os}')".format(mediation_sdk_version = row['mediation_sdk_version'], ad_network = row['ad_network'], adapter_version = row['adapter_version'], os = row['os']))
    query_string = """
    truncate mobile_bi.tams_sdk_compatibility;
    insert into mobile_bi.tams_sdk_compatibility (mediation_sdk_version,ad_network,adapter_version,os) values {rows}"""
    return query_string

query_string = update_redshift_db()
print(query_string)
    #open db connection
    # path = 'c:/Users/admin/Documents/Python Scripts/redshift/ssd_redshift.yml'#.format(USER=os.environ['USER'])
    # config = yaml.safe_load(open(path))['ssd_redshift']
    # conn_string = "dbname={dbname} port={port} user={user} password={password} host={host}".format(
    #     dbname=config['dbname'], port=config['port'], user=config['user'],
    #     password=config['password'], host=config['host'])
    # conn = psycopg2.connect(conn_string)
    # cursor = conn.cursor()
    # cursor.execute(query_string.format(rows = ','.join(row_data)))
    # conn.commit()
    # cursor.close()
