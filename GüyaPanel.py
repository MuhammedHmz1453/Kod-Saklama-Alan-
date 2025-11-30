import xml.etree.ElementTree as ET
import requests

url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
headers = {"content-type": "text/xml"}

# Change this
tc_no = "XXXXXXXXXXXX"
ad = "NAME"
soyad = "SURNAME"
dogum_yili = 1995

body = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo>{tc_no}</TCKimlikNo>
      <Ad>{ad}</Ad>
      <Soyad>{soyad}</Soyad>
      <DogumYili>{dogum_yili}</DogumYili>
    </TCKimlikNoDogrula>
  </soap:Body>
</soap:Envelope>"""

r = requests.post(url, data=body, headers=headers)

root = ET.fromstring(r.text)

if root.find(".//soap:Fault", namespaces={"soap": "http://schemas.xmlsoap.org/soap/envelope/"}):
    fault_element = root.find(".//faultstring")
    error_message = fault_element.text
    print("Error:", error_message)
else:
    result_element = root.find(".//{http://tckimlik.nvi.gov.tr/WS}TCKimlikNoDogrulaResult")
    result = result_element.text
    print(result)