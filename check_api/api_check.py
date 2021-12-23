import sys
import os
import hashlib
import hmac
import base64
import requests
import time
import json
import datetime
#Return 'False' have Service, 'True' haven't service

# Object Storage, 
class api_check:

    
    def __init__(self,access,secret):
        self.access=access
        self.secret=secret

           
    def vpc_check(self):

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/vpc/v2/getVpcList?responseFormatType=json"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://ncloud.apigw.ntruss.com/vpc/v2/getVpcList?responseFormatType=json' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)
        res.request 

        if res.status_code != 200:
            print("Check Access & Secret Key")
            exit()
        total_row=res.json()['getVpcListResponse']['totalRows']
        if total_row >= 1:
            # Have VPC
            return False
        else:
            #Haven't VPC
            return True

        
        
    def server_check(self):

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/vserver/v2/getServerInstanceList?responseFormatType=json"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://ncloud.apigw.ntruss.com/vserver/v2/getServerInstanceList?responseFormatType=json' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)

        res.request 
        total_row=res.json()['getServerInstanceListResponse']['totalRows']
        if total_row >= 1:
            return False
        else:
            return True

    
    def lb_check(self):
     
        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/vloadbalancer/v2/getLoadBalancerInstanceList?responseFormatType=json"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://ncloud.apigw.ntruss.com/vloadbalancer/v2/getLoadBalancerInstanceList?responseFormatType=json' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)
        res.request 

        total_row=res.json()['getLoadBalancerInstanceListResponse']['totalRows']
        if total_row >= 1:
            return False
        else:
            return True

    
    def cdb_check(self):

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/vmysql/v2/getCloudMysqlInstanceList?responseFormatType=json"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://ncloud.apigw.ntruss.com/vmysql/v2/getCloudMysqlInstanceList?responseFormatType=json' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)
        res.request 

        if res.status_code != 200:
            print("Check Access & Secret Key")
            exit()
    
        total_row=res.json()['getCloudMysqlInstanceListResponse']['totalRows']
        if total_row >= 1:
            return False
        else:
            return True

    def gdns_check(self):

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/dns/v1/ncpdns/lb-record/VPC/A"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://globaldns.apigw.ntruss.com/dns/v1/ncpdns/lb-record/VPC/A' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)
        res.request 

        if res.status_code != 200:
            print("Check Access & Secret Key")
            exit()
        #total_row type is list
        total_row=res.json()

        #check dns 
        if total_row == []:
            return True
        else:
            return False
     


    def subaccount_check(self):

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/api/v1/login-alias"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://subaccount.apigw.ntruss.com/api/v1/login-alias' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)
        res.request 

        if res.status_code != 200:
            print("Check Access & Secret Key")
            exit()
        #result type is list
        result=res.json()

        #check sub_account 
        if result == {}:
            return True
        else:
            return False


    def nas_check(self):

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
            
        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        secret_key = bytes(secret_key).encode("utf-8")

        method = "GET"
        uri = "/vnas/v2/getNasVolumeInstanceList?responseFormatType=json"

        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message).encode("utf-8")
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
        URL = 'https://ncloud.apigw.ntruss.com/vnas/v2/getNasVolumeInstanceList?responseFormatType=json' 

        headers = {'x-ncp-apigw-timestamp': timestamp, 
                   'x-ncp-iam-access-key':  access_key,
                   'x-ncp-apigw-signature-v2': signingKey
                   }

        # 'Content-Type': 'application/json; UTF-8'
        res = requests.get(URL, headers=headers)
        res.request 

        if res.status_code != 200:
            print("Check Access & Secret Key")
            exit()

        #result type is list
        total_row=res.json()['getNasVolumeInstanceListResponse']['totalRows']
        if total_row >= 1:
            return False
        else:
            return True


    def sign(self, key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def getSignatureKey(self, key, dateStamp, regionName, serviceName):

        kDate = self.sign(('AWS4' + key).encode('utf-8'), dateStamp)
        kRegion = self.sign(kDate, regionName)
        kService = self.sign(kRegion, serviceName)
        kSigning = self.sign(kService, 'aws4_request')
        return kSigning

    
    def object_storage_check(self):

        method = 'GET'
        service = 's3'
        host = 'kr.object.ncloudstorage.com'
        region = 'us-east-1'
        endpoint = 'https://kr.object.ncloudstorage.com'
        request_parameters = 'Action=DescribeRegions&Version=2013-10-15'

        access_key = self.access	# access key id (from portal or Sub Account)
        secret_key = self.secret   # secret key (from portal or Sub Account)
        if access_key is None or secret_key is None:
            print('No access key is available.')
            sys.exit()


        t = datetime.datetime.utcnow()
        amzdate = t.strftime('%Y%m%dT%H%M%SZ')
        datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope

        canonical_uri = '/' 
        canonical_querystring = request_parameters
        canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
        
        signed_headers = 'host;x-amz-date'
        payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()
        canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
        string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()




        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
        string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()


        signing_key = self.getSignatureKey(secret_key, datestamp, region, service)

        signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

        headers = {

                   'Authorization' :authorization_header,
                    'Host' : host,
                    'x-amz-date' : 	amzdate
                   }

        # 'Content-Type': 'application/json; UTF-8'

        request_url = endpoint + '?' + canonical_querystring

        res = requests.get(request_url, headers=headers)
        

         
        if res.status_code == 403:
            return True

        if len(res.text) > 300:
            return False
        else:
           return True


if __name__ == "__main__":

    if len(sys.argv) <=2:
        print("Write Access Key and Secret Key plz")
    else:   
        start = time.time() 

        a = sys.argv[1]
        b = sys.argv[2]
        test=api_check(a,b)
        

        dict={'vpc': 0,
              'server': 0,
              'Load Balancer': 0,
              'Cloud DB for MySQL': 0,
              'Object Storage': 0,
              'NAS': 0,
              'Sub Account': 0,
              'GDNS': 0      
            } 

        vpc=0
        server=0
        lb=0
        cbd=0
        os=0
        nas=0
        subaccount=1000000
        gdns=10000000

        if test.vpc_check()==False:
            vpc=1
        else:
            print("00000000")
            quit()
        if test.server_check()==False:
            server=10
        if test.lb_check()==False:
            lb=100
        if test.cdb_check()==False:
            cbd=1000
        if test.nas_check()==False:
            nas=100000


        if test.object_storage_check()==False:
            os=10000

        if test.subaccount_check()==False:
            subaccount=1000000
        if test.gdns_check()==False:
            gdns=10000000

        total= vpc + server + lb + cbd + os + nas + subaccount + gdns
        
        print(total)

        #print("time :", time.time() - start)  
