#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class ExportPipeline(catoclient.catocommand.CatoCommand):

    Description = 'Exports a Pipeline backup file.  Includes complete versions of all Phases and Stages.'
    API = 'export_pipeline'
    Examples = '''
_To export a Pipeline backup file._

    csk-export-pipeline -p "MyPipeline" > mypipeline.json 
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['pipeline'])
        print(results)
