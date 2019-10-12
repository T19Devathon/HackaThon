from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/ABCinsurance')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-793111792757-793108047152-794966304887-1b64bb6fc811033aed29a3a7bf1ddf99', #app verification token
							'xoxb-793111792757-793110383952-QX41DVOU6lTXa7NLRJwWP2UK', # bot verification token
							'nk6GcEF7lId6CM4ewTi1vY2w', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))