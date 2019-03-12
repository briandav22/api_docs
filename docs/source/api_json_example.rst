JSON Example
=============

Example of JSON returned by the Scrutinizer API. 

.. code-block:: json

    {
        "report": {
            "table": {
            "inbound": {
                "totalRowCount": "38",
                "columns": [
                {
                    "title": "Rank",
                    "label": "",
                    "klassth": "rankWidth"
                },
                {
                    "colHasBbp": 0,
                    "defaultSort": null,
                    "klassth": "",
                    "klassLabel": "",
                    "format": {},
                    "elementName": "applicationid",
                    "canBeRate": null,
                    "label": "Application",
                    "title": "applicationid"
                },
                {
                    "colHasBbp": 0,
                    "defaultSort": null,
                    "klassth": "alignRight ",
                    "klassLabel": "",
                    "format": {},
                    "elementName": "percenttotal",
                    "canBeRate": null,
                    "label": "Traffic %",
                    "title": "percenttotal"
                },
                {
                    "colHasBbp": 1,
                    "forceLabel": "Peak",
                    "defaultSort": null,
                    "klassth": "alignRight",
                    "klassLabel": "",
                    "format": {
                    "isRate": 0,
                    "niceLtr": "%",
                    "perSecMode": 0
                    },
                    "elementName": "rpt_man_peak",
                    "canBeRate": 1,
                    "label": "Peak",
                    "title": "rpt_man_peak"
                },
                {
                    "colHasBbp": 1,
                    "forceLabel": "95th",
                    "defaultSort": null,
                    "klassth": "alignRight",
                    "klassLabel": "",
                    "format": {
                    "isRate": 0,
                    "niceLtr": "%",
                    "perSecMode": 0
                    },
                    "elementName": "rpt_man_95th",
                    "canBeRate": 1,
                    "label": "95th",
                    "title": "rpt_man_95th"
                },
                {
                    "colHasBbp": 1,
                    "defaultSort": "DESC",
                    "klassth": "alignRight  sortable  hasBbp ",
                    "klassLabel": " sortdesc ",
                    "format": {
                    "isRate": 0,
                    "niceLtr": "%",
                    "perSecMode": 0
                    },
                    "elementName": "sum_octetdeltacount",
                    "canBeRate": 1,
                    "label": "% Util.",
                    "title": "sum_octetdeltacount"
                },
                {
                    "elementName": "first_flow_epoch",
                    "label": "first_flow_epoch"
                },
                {
                    "elementName": "last_flow_epoch",
                    "label": "last_flow_epoch"
                }
                ],
                "rows": [
                [
                    {
                    "klasstd": "rank1",
                    "title": "Rank: 1",
                    "label": "1"
                    },
                    {
                    "rawValue": "ipfix (4739 - UDP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "ipfix (4739 - UDP)",
                    "label": "ipfix (4739 - UDP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "56.45 %",
                    "label": "56.45 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "4759190101",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank2",
                    "title": "Rank: 2",
                    "label": "2"
                    },
                    {
                    "rawValue": "NetFlow (Defined application)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "NetFlow (Defined application)",
                    "label": "NetFlow (Defined application)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "25.37 %",
                    "label": "25.37 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "2138712109",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank3",
                    "title": "Rank: 3",
                    "label": "3"
                    },
                    {
                    "rawValue": "globe (2002 - UDP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "globe (2002 - UDP)",
                    "label": "globe (2002 - UDP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "16.88 %",
                    "label": "16.88 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1422960799",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank4",
                    "title": "Rank: 4",
                    "label": "4"
                    },
                    {
                    "rawValue": "HTTP (80 - TCP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "HTTP (80 - TCP)",
                    "label": "HTTP (80 - TCP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.40 %",
                    "label": "0.40 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "34024556",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank5",
                    "title": "Rank: 5",
                    "label": "5"
                    },
                    {
                    "rawValue": "HTTPS (443 - UDP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "HTTPS (443 - UDP)",
                    "label": "HTTPS (443 - UDP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.25 %",
                    "label": "0.25 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "21315903",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank6",
                    "title": "Rank: 6",
                    "label": "6"
                    },
                    {
                    "rawValue": "HTTPS (443 - TCP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "HTTPS (443 - TCP)",
                    "label": "HTTPS (443 - TCP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.24 %",
                    "label": "0.24 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "20270540",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank7",
                    "title": "Rank: 7",
                    "label": "7"
                    },
                    {
                    "rawValue": "ipsec-nat-t (4500 - UDP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "ipsec-nat-t (4500 - UDP)",
                    "label": "ipsec-nat-t (4500 - UDP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.22 %",
                    "label": "0.22 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "18429492",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank8",
                    "title": "Rank: 8",
                    "label": "8"
                    },
                    {
                    "rawValue": "irdmi (8000 - UDP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "irdmi (8000 - UDP)",
                    "label": "irdmi (8000 - UDP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.12 %",
                    "label": "0.12 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "9973109",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408560",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408560",
                    "label": "1552408560"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank9",
                    "title": "Rank: 9",
                    "label": "9"
                    },
                    {
                    "rawValue": "Maximizer (Defined application)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "Maximizer (Defined application)",
                    "label": "Maximizer (Defined application)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.03 %",
                    "label": "0.03 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "2931261",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ],
                [
                    {
                    "klasstd": "rank10",
                    "title": "Rank: 10",
                    "label": "10"
                    },
                    {
                    "rawValue": "SSH (22 - TCP)",
                    "dataJson": "{\"column\":\"applicationid\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "SSH (22 - TCP)",
                    "label": "SSH (22 - TCP)"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"percenttotal\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "0.01 %",
                    "label": "0.01 %"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_peak\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": null,
                    "dataJson": "{\"column\":\"rpt_man_95th\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "Value undefined",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1049476",
                    "dataJson": "{\"column\":\"sum_octetdeltacount\"}",
                    "klasstd": "alignRight",
                    "klassLabel": "",
                    "title": "--",
                    "label": "NA"
                    },
                    {
                    "rawValue": "1552408380",
                    "dataJson": "{\"column\":\"first_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408380",
                    "label": "1552408380"
                    },
                    {
                    "rawValue": "1552408920",
                    "dataJson": "{\"column\":\"last_flow_epoch\"}",
                    "klasstd": "alignLeft",
                    "klassLabel": "",
                    "title": "1552408920",
                    "label": "1552408920"
                    }
                ]
                ],
                "footer": [
                [
                    {
                    "title": "Other",
                    "label": "Other"
                    },
                    {
                    "klasstd": "alignLeft",
                    "translations": "",
                    "elementName": "applicationid",
                    "title": "Group by columns are not summarized",
                    "label": " ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignRight",
                    "translations": "",
                    "elementName": "percenttotal",
                    "title": "Group by columns are not summarized",
                    "label": " ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignLeft",
                    "translations": "",
                    "elementName": "rpt_man_peak",
                    "title": "Group by columns are not summarized",
                    "label": " - ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignLeft",
                    "translations": "",
                    "elementName": "rpt_man_95th",
                    "title": "Group by columns are not summarized",
                    "label": " - ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignRight",
                    "translations": "",
                    "elementName": "sum_octetdeltacount",
                    "title": "--",
                    "label": " - ",
                    "menuType": "",
                    "filterType": ""
                    }
                ],
                [
                    {
                    "title": "(from conv tables)",
                    "label": "Total*"
                    },
                    {
                    "klasstd": "alignLeft",
                    "translations": "",
                    "elementName": "applicationid",
                    "title": "Group by columns are not summarized",
                    "label": " ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignRight",
                    "translations": "",
                    "elementName": "percenttotal",
                    "title": "Group by columns are not summarized",
                    "label": " ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignRight",
                    "translations": "",
                    "elementName": "rpt_man_peak",
                    "title": "Group by columns are not summarized",
                    "label": " - ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignRight",
                    "translations": "",
                    "elementName": "rpt_man_95th",
                    "title": "Group by columns are not summarized",
                    "label": " - ",
                    "menuType": "",
                    "filterType": ""
                    },
                    {
                    "klasstd": "alignRight",
                    "translations": "",
                    "elementName": "sum_octetdeltacount",
                    "title": "--",
                    "label": " - ",
                    "menuType": "",
                    "filterType": ""
                    }
                ]
                ]
            }
            },
            "request_id": "0x06cef15a44e611e9bd65f7a0e9da3b22",
            "time_details": {
            "timezone": "EDT",
            "last_time": {
                "epoch": "1552408920",
                "formatted": "2019-03-12 12:42:00"
            },
            "first_time": {
                "epoch": "1552408380",
                "formatted": "2019-03-12 12:33:00"
            }
            },
            "exporter_details": {
            "10.1.1.252": {
                "flow_count": 664,
                "exporter_hex": "0A0101FC"
            }
            }
        }
    }