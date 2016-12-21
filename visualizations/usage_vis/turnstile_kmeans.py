# K-means clustering on subway turnstiles
from sklearn.cluster import Kmeans
import urllib.request
import json
import dml
import prov.model
import datetime
import uuid
import pandas as pd

class turnstile_kmeans(dml.Algorithm):
	contributor = 'anuragp1_jl101995'
	reads = ['anuragp1_jl101995.geocoded_turnstile']

	@staticmethod
	def execute():

		startTime = datetime.datetime.now()

        # Set up the database connection.
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('anuragp1_jl101995', 'anuragp1_jl101995')

        print('Loading citibike_data from Mongo')
        geoturnstile_data = repo.anuragp1_jl101995.geocoded_turnstile.find()

        











