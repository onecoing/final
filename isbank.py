 datem = datetime.today().strftime('%Y-%m-%d')
        strdate="/v1/exchange-rates/EUR/?date="+datem
        conn = http.client.HTTPSConnection("api.sandbox.isbank.com.tr")
        headers = {
            'x-ibm-client-id': "3fea0e12-e129-44ef-8378-9f835adfe245",
            'x-ibm-client-secret': "E8nI1iK4uD7uF3rI4xN5cE6rF0lK1gU5aE4sP7nD0bG6yT4bP7"
                }
        conn.request("GET", strdate, headers=headers)
        res = conn.getresponse()
        data = res.read()
        kurlar = (data.decode("utf-8"))
        my_json = kurlar.replace("'", '"')
        datax = json.loads(my_json)
        s = json.dumps(datax, indent=4, sort_keys=True)
        eurokur=(datax['data']['effective_rate_sell'])
        eurokur=float(eurokur)
        onek = eurokur * 42.43