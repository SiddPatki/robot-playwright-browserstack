from browserstack.local import Local
import json
import urllib.parse
import subprocess
import os


class CustomLib:
    desired_cap = {
    'os': 'os x',
    'os_version': 'Ventura',
    'browser': 'playwright-webkit',  # allowed browsers are `chrome`, `edge`, `playwright-chromium`, `playwright-firefox` and `playwright-webkit`
    'browserstack.username': os.environ['BROWSERSTACK_USERNAME'],
    'browserstack.accessKey': os.environ['BROWSERSTACK_ACCESS_KEY'],
    'project': 'BStack Project',
    'build': 'browserstack-build-11',
    'buildTag': 'Regression',
    'resolution': '1280x1024',
    'browserstack.playwrightVersion': '1.latest',
    'client.playwrightVersion': '1.latest',
    'browserstack.debug': 'true',  # enabling visual logs
    'browserstack.console': 'info',  # Enabling Console logs for the test
    'browserstack.networkLogs': 'true',  # Enabling network logs for the test
    'browserstack.networkLogsOptions':
        {
            'captureContent': 'true'
        }
    }


    def createCdpUrl(self):
        # clientPlaywrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        # CustomLib.desired_cap['client.playwrightVersion'] = clientPlaywrightVersion
        cdpUrl = 'wss://cdp.browserstack.com/playwright?caps=' + urllib.parse.quote(json.dumps(CustomLib.desired_cap))
        print(cdpUrl)
        return cdpUrl
    
    def getPlatformDetails(self):
        platformDetails = CustomLib.desired_cap['os'] + " " + CustomLib.desired_cap['os_version']+ " " + CustomLib.desired_cap['browser']
        # platformDetails = CustomLib.desired_cap['os'] + " " + CustomLib.desired_cap['os_version']+ " " + CustomLib.desired_cap['browser']+ " " + CustomLib.desired_cap['browser_version']
        print(platformDetails)
        return platformDetails
    
    def startLocalTunnel(self):
        # Creates an instance of Local
        self.bs_local = Local()
        # You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
        bs_local_args = { "key": os.environ['BROWSERSTACK_ACCESS_KEY'], "forcelocal": "true" }
        # Starts the Local instance with the required arguments
        self.bs_local.start(**bs_local_args)
        # Check if BrowserStack local instance is running
        print("BrowserStackLocal running: " + str(self.bs_local.isRunning()))
    
    def stopLocalTunnel(self):
        self.bs_local.stop()

    