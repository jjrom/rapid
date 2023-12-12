"""
rapid - process.py
Copyright 2023 Jerome Gasperi
@author: jerome.gasperi@gmail.com
"""
import requests
import json
import os
import rapid.settings as settings

class ProcessAPI():
    
    def __init__(self, config=None):
        """
        Initialize Process class - access to resto OGC API Processes

        @params
            config          --  Superseed settings.config / environnment variables
                                Allowed variables are :
                                    RESTO_API_ENDPOINT
                                    RESTO_PROCESS_API_AUTH_TOKEN
                                    RESTO_PROCESS_API_S3_HOST
                                    RESTO_PROCESS_API_S3_BUCKET
                                    RESTO_PROCESS_API_S3_KEY
                                    RESTO_PROCESS_API_S3_SECRET
                                    RESTO_PROCESS_API_S3_REGION
        """
        
        self.config = {}
        
        configKeys = [
            'RESTO_API_ENDPOINT',
            'RESTO_PROCESS_API_AUTH_TOKEN',
            'RESTO_PROCESS_API_S3_HOST',
            'RESTO_PROCESS_API_S3_BUCKET',
            'RESTO_PROCESS_API_S3_KEY',
            'RESTO_PROCESS_API_S3_SECRET',
            'RESTO_PROCESS_API_S3_REGION'
        ]
        for key in configKeys:
            self.config[key] = os.environ.get(key) if os.environ.get(key) else settings.config[key]
            if config and key in config:
                self.config[key] = config[key]
        
        self.processAPIUrl = self.config['RESTO_API_ENDPOINT'] + '/oapi-p/processes'
        
        print(self.config)
 
        
    def deploy(self, process_metadata, execution_unit):
        """
        Deploy input process as an Application Package to resto endpoint

        @params
            process_metadata    -- Process metadata
            execution_unit      -- Execution unit metadata
        """
        
        body = {
            'processDescription': process_metadata,
            'executionUnit': execution_unit
        }
        
        return requests.post(self.processAPIUrl,
        	data=json.dumps(body),
        	headers={
                'Content-Type': 'application/json',
                'Content-Length': str(len(body)),
                'Authorization': 'Bearer ' + (self.config['RESTO_PROCESS_API_AUTH_TOKEN'] if self.config['RESTO_PROCESS_API_AUTH_TOKEN'] != None else 'none')
            }
        )
