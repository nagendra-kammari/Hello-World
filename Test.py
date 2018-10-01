import googleapiclient.discovery

compute = googleapiclient.discovery.build('compute', 'v1')

#Instances = compute.instances().list(project="perceptive-zoo-218002", zone="asia-south1-c").execute()
#print (Instances)

image_response = compute.images().getFromFamily(project='ubuntu-os-cloud', family='ubuntu-1804-lts').execute()
image_source=image_response['selfLink']

print (image_source)
