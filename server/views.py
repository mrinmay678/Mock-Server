from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MockServerView(APIView):

    def post(self, request, service=None):
    
        if not service:
            return Response(status=400)
        elif service == "signup" or service == "login":
            data= {
                "status": "success",
                "data": {
                    "access_token": "onvonvlkfdsnssssvlkfdveo3ionqnvv;mevmpfmvpfdplfdnlkdfnvodvmdffds",
                    "refresh_token": "onvonvlkfdsnvlkfdveo3ionqnvv;mevmpfmvpfdplfdnlkdfnvodvmdffds"
                }
            }
        elif service == "refresh-token":
            data={
                "access_token": "onvonvlkfdsnvlkfddcdwdveo3ionqnvv;mevmpfmvpfdplfdnlkdfnvodvmdffds"
            }
        
        return Response({"status":True,"data":data})

    def get(self, request, service=None):

        if not service:
            return Response(status=400)
        elif service == "location":
            data={
                "locations": [
                    {
                        "country": "India",
                        "cities": [
                        {
                            "name": "Kolkata",
                            "id": "CCU"
                        },
                        {
                            "name": "Mumbai",
                            "id": "MUM"
                        },
                        {
                            "name": "New Delhi",
                            "id": "NDLS"
                        },
                        {
                            "name": "Bangalore",
                            "id": "BNGL"
                        },
                        {
                            "name": "Hyderabad",
                            "id": "HYD"
                        },
                        {
                            "name": "Agartala",
                            "id": "AGTL"
                        }
                        ]
                    },
                    {
                        "country": "United States of America",
                        "cities": [
                        {
                            "name": "New York City",
                            "id": "NYC"
                        },
                        {
                            "name": "Washington D.C.",
                            "id": "WDC"
                        },
                        {
                            "name": "Los Angeles",
                            "id": "LA"
                        }
                        ]
                    }
                ]
            }
        elif service == "flights":
            data= {
                "flights": [
                    {
                        "id": 1,
                        "flight_name": "Air India",
                        "dept": "21 April 2021 12:00",
                        "arr": "21 April 2021 14:00",
                        "cost": "Rs. 5199"
                    },
                    {
                        "id": 2,
                        "flight_name": "Air India",
                        "dept": "12 Jun 2021 10:00",
                        "arr": "12 Jun 2021 14:00",
                        "cost": "Rs. 3499"
                    },
                    {
                        "id": 3,
                        "flight_name": "Indigo",
                        "dept": "12 July 2021 9:00",
                        "arr": "12 July 2021 10:30",
                        "cost": "Rs. 4290"
                    },
                    {
                        "id": 4,
                        "flight_name": "SpiceJet",
                        "dept": "12 March 2021 11:00",
                        "arr": "12 March 2021 13:00",
                        "cost": "Rs. 4699"
                    },
                    {
                        "id": 5,
                        "flight_name": "SpiceJet",
                        "dept": "12 Jan 2021 16:00",
                        "arr": "12 Jan 2021 18:00",
                        "cost": "Rs. 3699"
                    },
                    {
                        "id": 6,
                        "flight_name": "SpiceJet",
                        "dept": "12 May 2021 21:00",
                        "arr": "13 May 2021 02:00",
                        "cost": "Rs. 4199"
                    }
                ]
            }

        elif service == "profile":
            data= {
                "first_name": "Airways",
                "last_name": "SAMP",
                "email": "aniruddha.nath21@gmail.com",
                "dob": "2.2.2002",
                "country_code": "+91",
                "phone_number": "987654321",
                "flights": [
                    {
                        "id": 1,
                        "flight_name": "Air India",
                        "source": "Kolkata",
                        "dest": "New Delhi",
                        "depart": "21 April 2021 12:00",
                    },
                    {
                        "id": 2,
                        "flight_name": "Air Asia",
                        "source": "Kolkata",
                        "dest": "Mumbai",
                        "depart": "11 April 2021 15:00",
                    },
                    {
                        "id": 3,
                        "flight_name": "Air India",
                        "source": "Kolkata",
                        "dest": "Bangalore",
                        "depart": "10 Jan 2021 08:00",
                    },
                    {
                        "id": 4,
                        "flight_name": "Air India",
                        "source": "Kolkata",
                        "dest": "Hyderabad",
                        "depart": "10 Jan 2021 18:00",
                    }
                ]
            }
        elif service == "flight":
            data={
                "flight_name": "Air India",
                "source": "Kolkata",
                "destination": "New Delhi",
                "adult": 1,
                "child": 0,
                "departure": "2018-12-12 12:00:00",
                "arrival": "2018-12-12 13:00:00",
                "price": "2000"
            }
        
        return Response({"status":True,"data":data})