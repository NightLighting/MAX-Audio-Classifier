#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from maxfw.core import MAXApp
# from api import ModelMetadataAPI, ModelPredictAPI
from api import ModelPredictAPI
from config import API_TITLE, API_DESC, API_VERSION

os.environ['CORS_ENABLE']='true'
os.environ['WERKZEUG_RUN_MAIN']='true'

max_app = MAXApp(API_TITLE, API_DESC, API_VERSION)
# max_app.add_api(ModelMetadataAPI, '/metadata')
max_app.add_api(ModelPredictAPI, '/predict')
max_app.run()
