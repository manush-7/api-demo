from datetime import datetime
import json
import pytz
import pymysql
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
import csv
import boto3
s3_client = boto3.client('s3')
def execute_select(dbConnection,select_query):
    global header
    global query_count   
    try:
        with dbConnection.cursor() as curObj:
            curObj.execute(select_query)
            query_count = curObj.rowcount
            return curObj.fetchall()
    except Exception as e:
        logger.error(e)
    else:
        logger_info.extend(["SELECT query executed successfully."])

def write_tmp(res,Key):
    try:
        with open('/tmp/'+Key, 'w') as fileout:
            writer = csv.writer(fileout,delimiter='|')
            writer.writerows(res)
            return '/tmp/'+Key
    except Exception as e:
        logger.error(e)
    else:
        logger_info.extend(["File written into /tmp/ successfully."])

def write_s3(Bucket,Prefix,Source,Sink):
    try:
        s3_client.put_object(Body=open(Source, 'rb'), Bucket=Bucket, Key=Sink)
    except Exception as e:
        logger.error(e)
    else:
        logger_info.extend(["File written into s3 bucket. " + Bucket + " " + Prefix + " " +Sink])

def extract(event, bucket):
    print(' ## STARTING OF HANDLER FUNCTION ##')
    date = event["queryStringParameters"]["date"]
    print(date)
    global connection, file_time_format,logger_info
    logger_info = []
    # TIME FORMAT
    ist = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(ist)
    file_time_format = datetime_ist.strftime('%Y%m%d_%H%M%S')
    # TIME FORMAT
    """
    Create DB connection 
    """
    try:
        dbConnection = pymysql.connect(
        host='paccar-test-mysql-db.chazdlreh5oz.us-west-2.rds.amazonaws.com',
        user='admin', 
        password = "qwertyuiop",
        db='test',
        )
    except Exception as e: 
      logger.error(e)
      logger_info.extend(["ERROR: Unexpected error: NOT CONNECTED"])
    else:
      logger_info.extend(["Connection to RDS mysql instance succeeded"])
      logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
    """
    End DB connection
    """
    ## DUMMY SELECT QUERY CHANGE ACCORDING TO YOUR REQUIREMENT 
    select_query = "SELECT * FROM Employees"
    try:
        sql_response = execute_select(dbConnection,select_query)
        print(query_count)
        if query_count > 1:
            ## CREATING TEMP FILE
            csv_out = write_tmp(res=sql_response,Key='MY_FIRST_EXTRACT')
            final_output_filename = 'rds_to_s3_'+file_time_format
            print(csv_out)
            ## Loadinf file to s3
            s3_out = write_s3(Bucket='paccar-test-mysql-to-s3', \
            Prefix = 'rds_to_s3/output', \
            Source = csv_out, \
            Sink= 'rds_to_s3/output/'+ final_output_filename+'.txt')
            return {
                'statusCode': 200
            }   
    except Exception as e:
        logger.error(e)
        logger_info.append(["Error executing lambda handler",str(e)])