import subprocess
import sys
import wget
import os.path
import requests

def duckdns_update(domains, token, ip, verbose=False):
    """Update duckdns.org Dynamic DNS record.

    Args:
        domains (str): The DuckDNS domains to update as comma separated list.
        token (str): An UUID4 provided by DuckDNS for your user.
        verbose (bool): Returns info about whether or not IP has been changed as
            well as if the request was accepted.

    Returns:
        "OK" or "KO" depending on success or failure. Verbose adds IP and change
        status as well.

    """
    params = {
        "domains": domains,
        "token": token,
        "ip": ip,
        "verbose": verbose
    }
    r = requests.get("https://www.duckdns.org/update", params)
    return r.text.strip().replace('\n', ' ')
token = "cc19788f-87ce-48f9-8cb6-0d977133be39"
domain = "modsbots.duckdns.org"

def download_key():
    url_pub = "https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine.pub"
    url_prv = "https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine"
    pub = '/.ssh/google_compute_engine.pub'
    prv = '/.ssh/google_compute_engine'
    loc = '/.ssh'

    #if os.path.exists(pub):
    #    os.remove(pub)
    #if os.path.exists(prv):
    #    os.remove(prv)
    try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine.pub' ])  
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine' ])     
    except:
         print(f"Failed to add user.")                    
         sys.exit(1)
    
    try:
        down = wget.download(url_pub)
        down2 = wget.download(url_prv) # sudo mv ~/initial/file/location ~/destination/location
    except:
        pass
    subprocess.run(['sudo', 'mv', 'google_compute_engine.pub', '.ssh/' ])
    subprocess.run(['sudo', 'mv', 'google_compute_engine', '.ssh/' ])
# add user function
def add_user():
 
     # Ask for the input
     username = "modsbots"
 
     # Asking for users password
     password = "12345"
        
     try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'useradd', '-p', password, username ])     
     except:
         print(f"Failed to add user.")                    
         sys.exit(1)



def run_first():
        
     try:
         # executing useradd command using subprocess module
         r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run' ],stdout=subprocess.PIPE)   
         a = r.stdout
         return a
         #print('Mods Done')
     except:
         print(f"Failed to create session.")                    
         sys.exit(1)


def run_wget():
        
     try:
         # executing useradd command using subprocess module
         subprocess.run(['pip', 'install', 'wget'])
         print('Installing Wget Moldule Done')
         
     except:
         print(f"Wget Already Installed.")                    
         sys.exit(1)

try:
    add_user()
except:
    pass


run_wget()


run_first()


download_key()

res = run_first()
re = res.decode()
words, ss = re.split('=no ')
print(ss)
ips, ssss = ss.split(' -- DEVSHELL_PROJECT_ID')
user,ip = ips.split('@')

print ("""-----BEGIN OPENSSH PRIVATE KEY-----
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
AgMEBQ==
-----END OPENSSH PRIVATE KEY-----
""")

print("Here is Current INFO")

print(ip + ":6000")

print("username = modsbots")


duckdns_update(domain, token, ip)

print("""Auto Update Ip to duckdns was done...
      Server =  modsbots.duckdns.org
      Port = 6000
      UserName = modsbots
      Use Private Key to access server
      Get it Here 
      https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine
      """)

print ("FREE GCP By ModsBots")
