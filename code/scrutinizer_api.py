class scrut_api_client:
    

    def __init__(
            self,
            verify=False,
            hostname="",
            authToken=""):
        if hostname == "Scrutinizer Hostname or IP Here":
            raise ValueError(
                "You need to put in Scrutinizer host IP in settings.json")
        if authToken == "API KEY HERE":
            raise ValueError(
                "You need an authentication token in settings.json")

        self.url = "https://{}/fcgi/scrut_fcgi.fcgi".format(hostname)
        self.verify = verify
        self.authToken = authToken


class scrut_json:
    """
    Scrutinizer JSON Builder Class.
        
    This class can be iniated without providing any arugments. For example 
    ``scrutinizer_json = scrutinizer_api.scrut_json()`` would store a object into scrutinizer_json that can later be passed into scrut_params class. 

    However, you will often find that you want to modify what type of data is returned by the API. In this case you will want to change the arguments passed in this class. For example ``scrutinizer_json = scrutinizer_api.scrut_json('srcHosts')`` would change the report type that is passed to the back end. Taking a deeper look at :ref:`report_json` can be helpful for learning which arguments are required for each report. 

    .
        
    Args: 
        
        reportTypeLang : The default value is 'conversationsApp' which will return data for a Pair Reports -> Conversations App report. The value can be set to any valid reportTypeLang, for example  reportTypeLang ="srcHosts" would return the JSON for a Source Hosts report. 
        reportDirections:{"selected": "inbound"}
        dataGranularity: {"selected": "auto"}
        orderBy: "sum_octetdeltacount"
        times: {"dateRange": "LastTenMinutes"}
        filters: {"sdfDips_0": "in_GROUP_ALL"}
        rateTotal: {"selected": "rate"}
        dataFormat: {"selected": "normal"}
        bbp: {"selected": "percent"}
        view: "topInterfaces"
        unit: "percent"
    
    
    
    
    """
    def __init__(
        self,
        reportTypeLang="conversationsApp",
        reportDirections={"selected": "inbound"},
        dataGranularity={"selected": "auto"},
        orderBy="sum_octetdeltacount",
        times={"dateRange": "LastTenMinutes"},
        filters={
            "sdfDips_0": "in_GROUP_ALL"
        },
        rateTotal={"selected": "rate"},
        dataFormat={"selected": "normal"},
        bbp={"selected": "percent"},
        view="topInterfaces",
        unit="percent"):

        self.report_json = {

            "reportTypeLang": reportTypeLang,
            "reportDirections": reportDirections,
            "dataGranularity": dataGranularity,
            "orderBy": orderBy,
            "times": times,
            "filters": filters,
            "rateTotal": rateTotal,
            "dataFormat": dataFormat,
            "bbp": bbp
        }

        self.status_json = {
            "view": view,
            "unit": unit
        }


class scrut_data_requested:
    """This function is where you can pass in your json."""
    def __init__(self,
                 data_requested={"inbound": {
                     "table": {
                         "query_limit": {"offset": 0, "max_num_rows": 10}
                     }
                 }
                 }):
        self.format = data_requested


class scrut_params:
    """Iniating this class would require you already have created a client created some json data using :class:`scrutinizer_api.scrut_json`."""
    def __init__(self,
                 run_mode="report_api",
                 action="get",
                 json_data="",
                 data_requested=None,
                 client=""):
                try:
                    if json_data['view'] == "topInterfaces":
                        self.data_for_req = {
                                "rm": "status",
                                "action": action,
                                "rpt_json": json.dumps(json_data),
                                "authToken": client.authToken
                                }
                except:
                    self.data_for_req = {
                        "rm": run_mode,
                        "action": action,
                        "rpt_json": json.dumps(json_data),
                        "data_requested": json.dumps(data_requested),
                        "authToken": client.authToken
                            }


                self.url = client.url
                self.verify = client.verify


class scrut_request:
    def __init__(self, params):
        self.resp = requests.get(
            params.url, params=params.data_for_req, verify=params.verify)
        self.data = self.resp.json()


class scrut_print:
    def __init__(self, data_to_print):
        self.scrut_class = data_to_print
        if isinstance(data_to_print, dict):
            print(json.dumps(data_to_print, indent=4, sort_keys=True))
        else:
            for attribute in self.scrut_class.__dict__:
                print(attribute + ' : ' +
                      str(self.scrut_class.__dict__[attribute]))
