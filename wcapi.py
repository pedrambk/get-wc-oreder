from woocommerce import API

wcapi = API(
    url="http://localhost",
    consumer_key="ck_148ab49b5f9f4401acbb5ef0ab3b83136111d226",
    consumer_secret="cs_f21eacc66c66236ff1289dc582ed63e44747b543",
    version="wc/v3"
)
r=wcapi.get("orders")
import pprint
pprint.pprint(r.json())

