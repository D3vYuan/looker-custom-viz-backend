<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Looker API</h2>
  <p align="center">
    Case Study - Looker API Look Information
  </p>
  <!--div>
    <img src="images/profile_pic.png" alt="Logo" width="80" height="80">
  </div-->
</div>

---

<!-- TABLE OF CONTENTS -->

## Table of Contents

<!-- <details> -->
<ol>
    <li>
        <a href="#about-the-project">About The Project</a>
    </li>
    <li>
        <a href="#setup">Setup</a>
        <ul>
            <li><a href="#bigquery">BigQuery</a></li>
            <li><a href="#looker">Looker</a></li>
            <li><a href="#looker-api">Looker API</a></li>
            <li><a href="#python-dependencies">Python Dependencies</a></li>
            <li><a href="#startup-script">Startup Script</a></li>
        </ul>
    </li>
    <li>
        <a href="#implementation">Implementation</a>
        <ul>
            <li><a href="#country-look">Get Country Look</a></li>
            <li><a href="#city-look">Get City Look</a></li>
        </ul>
    </li>
    <li><a href="#usage">Usage</a>
        <ul>
            <li><a href="#via-local">Via Local</a></li>
        </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>
<!-- </details> -->

---

<!-- ABOUT THE PROJECT -->

## About The Project

This project is created to showcase how we can `Looker API` to extract information from `Looker` for processing outside of `Looker` environment.

The following are some of the requirements:

- Extract the data information of a particular `Looker` looker view

`NOTE:` This repository is the backend, while the other [repository][ref-looker-custom-viz-frontend] is the frontend.

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- Setup -->

## Setup

Base on the requirements, the following components are required to be setup:

- `BigQuery` - To provide the sample data for `Looker`
- `Looker` - To construct the *Look* view so that the data can be query
- `Looker API` - To query `Looker` to get the relevant information
- `Python Dependencies` - The libraries required to run the application
- `Startup Script` - The script to run the application

<p align="right">(<a href="#top">back to top</a>)</p>

### BigQuery

For this case study, we will be using a public available data from the *data-to-insights.ecommerce*

View the public dataset by starring the *data-to-insights* dataset <br/>
| ![looker-bigquery-remote-dataset][looker-bigquery-remote-dataset] | 
|:--:| 
| *data-to-insights ecommerce data* |

<br/>

Copy the *data-to-insights* ecommerce data to a local dataset <br/>
`NOTE:` You might need to create the local dataset first
| ![looker-bigquery-remote-copy][looker-bigquery-remote-copy] | 
|:--:| 
| *data-to-insights ecommerce data copy* |

<br/>

Verify that the data are now in the local dataset together with the tables <br/>
| ![looker-bigquery-local-dataset][looker-bigquery-local-dataset] | 
|:--:| 
| *local ecommerce data* |

<p align="right">(<a href="#top">back to top</a>)</p>

### Looker

There will be 2 tasks to be done for `Looker`:
- *Generate Look View* - Create the `Look` view so that the data can be extracted using `Looker API`
- *Generate Access Token* - Generate the Client Id and Client Secret for the `Looker API`

<p align="right">(<a href="#top">back to top</a>)</p>

#### Generate Look View

For this case study, we will be using the *all_sessions* information to build 2 looks for data subsequently

`NOTE:` The look views are set to `public` accessible, and not tested with `private` view <br/>
<br/>
The *country view* consists of the *country* and *count* columns <br/>
| ![looker-look-country-view][looker-look-country-view] | 
|:--:| 
| *Look - Country View* |

<br/>

The *city view* consists of the *country*, *city* and *count* columns, with filter on the *country* and *city* columns <br/>
| ![looker-look-city-view][looker-look-city-view] | 
|:--:| 
| *Look - City View* |

<br/>

`NOTE:` In the subsequent session, the `Looker API` will need to know the respective `Look` view id, which can be found in the address bar area. <br/>
In the following example, the *country view* `Look` id is **163**
| ![looker-look-country-id][looker-look-country-id] | 
|:--:| 
| *Look - Country ID* |

<p align="right">(<a href="#top">back to top</a>)</p>

#### Generate Access Token
Generate access token for the user accessing `Looker API`. Under Admin > Locate the User Account to use for the `Looker API` > Click to see details of User Account > Under API Keys, click Edit Keys > Create New Keys <br/>

`NOTE:` You will need to assign the User Account with sufficient privileges to view the System Activities in `Looker` <br/>

| ![looker-api-user-account][looker-api-user-account] | 
|:--:| 
| *Looker API Client ID* |

<br/>

| ![looker-api-user-keys][looker-api-user-keys] | 
|:--:| 
| *Looker API Client Secret* |

<p align="right">(<a href="#top">back to top</a>)</p>

### Looker API

We will be using 2 methods from the `Looker API` to extract the information for the `Look` view:
- *get_look* - Get the metadata of the `Look` view
- *run_inline_query* - Get the data of the `Look` view

<p align="right">(<a href="#top">back to top</a>)</p>

#### get_look

The method *get_look* will be used to extract the metadata about the *Country* and *City* `Look` view, which will be used later to get the data from these looks.

| ![looker-api-explorer-gl-request][looker-api-explorer-gl-request] | 
|:--:| 
| *get_look request* |

<br/>

| ![looker-api-explorer-gl-response][looker-api-explorer-gl-response] | 
|:--:| 
| *get_look response* |

<p align="right">(<a href="#top">back to top</a>)</p>

#### run_inline_query
The method *run_inline_query* will be used to extract the data from the *Country* and *City* `Look` view<br/>

The following is a sample body for the *run_inline_query*: <br/>
`NOTE:` Minimally, the request body should contains *model*, *view*, and *fields*
```json
{
  "model": "bq-ecommerce-poc",
  "view": "all_sessions",
  "fields": ["all_sessions.country", "all_sessions.city", "all_sessions.count"]
}
```

| ![looker-api-explorer-riq-request][looker-api-explorer-riq-request] | 
|:--:| 
| *run_inline_query request* |

<br/>

| ![looker-api-explorer-riq-response][looker-api-explorer-riq-response] | 
|:--:| 
| *run_inline_query response* |

<p align="right">(<a href="#top">back to top</a>)</p>

### Python Dependencies

The following are the dependencies required for the program:

|#|Dependencies|Description|
|--|--|--|
|1|`looker-sdk`|`Looker API` python client library|
|2|`fastapi`|To create microservices in python|
|3|`pydantic`|To create object for microservices|
|4|`json-converter`|To map json from one format to another|
|5|`uvicorn`|To run the microservices|

<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

### Startup Script

We will be using the library *uvicorn* to serve the application endpoints. The following is the command to start:

```bash
python3 -m uvicorn looker_endpoint:app --reload
```

`NOTE:` We will be saving the commands in the *start_http.sh* for ease of resue later

<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Implementation

Base on the requirements, the following are the endpoints required:

- `Get Country Look` - Given a *look id*, return the data associated with the view
- `Get City Look` - Give a *look id* and a *country* as the filter, return the data associated with the view and the particular *country*

<p align="right">(<a href="#top">back to top</a>)</p>

### Country Look
This task make use of the `Looker API` to retrieve the data from the country look specify by the *look id* <br/>

```python
@app.post("/look/{id}/country")
async def get_look(id: int):
    filters={}
    print(f"Look #{id} with {filters}")
    look_query = LookQuery(id, filters)
    look_query_result = look_query.execute()
    country_transformation = CountryTransformation(look_query_result)
    response = country_transformation.processed_message
    return {"description": f"Look #{id} with {filters}",
            "response": f"{response}"}
```
<p align="right">(<a href="#top">back to top</a>)</p>

### City Look
This task make use of the `Looker API` to retrieve the data from the city look specify by the *look id* and filter them accordingly to the *country* filter provided<br/>

```python
@app.post("/look/{id}/city")
async def get_look(id: int, filter: CountryFilter):
    filters={filter.key: filter.value}
    filters["all_sessions.city"]="-'(not set)',-'not available in demo dataset'"
    print(f"Look #{id} with {filters}")
    look_query = LookQuery(id, filters)
    look_query_result = look_query.execute()
    city_transformation = CityTransformation(look_query_result)
    response = city_transformation.processed_message
    return {"description": f"Look #{id} with {filters}",
            "response": f"{response}"}
```
<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- USAGE EXAMPLES -->

## Usage

There are 1 mode to test out the implementation
- Running Locally by executing the *start_http.sh*

<p align="right">(<a href="#top">back to top</a>)</p>

### Via Local Run
The following are the execution steps to run the code locally:

- Download Packages in the *requirements.txt* for the program <br/>
    ```bash
    pip install -r requirements.txt
    ```
- Create a file from *looker.ini.example* and name it *looker.ini*. <br/>
Configure the Looker instance and API Client tokens information <br/>
`NOTE:` Change the looker instance port accordingly if a custom port is used
    ```
    base_url = https://<looker-instance>:19999
    client_id = <looker-api-client-id>
    client_secret = <looker-api-client-secret>
    ```

- Execute the startup script *start_http.sh* <br/>
    ```bash
    bash start_http.sh
    ```

- Verify that the program is started successfully <br/>
    **Logs** <br/>

    | ![looker-api-backend-run][looker-api-backend-run] | 
    |:--:| 
    | *Looker API Backend Run* |

- Verify that the program is running and return the *hello world* message with the following command: <br/>
    ```sh
    curl --location 'http://localhost:8000/'
    ```

    **Output** <br/>
    | ![looker-api-backend-test][looker-api-backend-test] | 
    |:--:| 
    | *Looker API Backend Test* |

<p align="right">(<a href="#top">back to top</a>)</p>

---
<!-- ACKNOWLEDGMENTS -->

## Acknowledgments
- [Looker API Look Data][ref-looker-api-look-data]
- [Readme Template][template-resource]

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[template-resource]: https://github.com/othneildrew/Best-README-Template/blob/master/README.md
[ref-looker-api-look-data]: https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/run_look_with_filters.py
[ref-looker-custom-viz-frontend]: https://github.com/D3vYuan/looker-custom-viz-frontend

[looker-bigquery-remote-dataset]: ./images/looker-bigquery-remote-dataset.png
[looker-bigquery-remote-copy]: ./images/looker-bigquery-remote-copy.png
[looker-bigquery-local-dataset]: ./images/looker-bigquery-local-dataset.png

[looker-look-country-view]: ./images/looker-look-country-view.png
[looker-look-city-view]: ./images/looker-look-city-view.png
[looker-look-country-id]: ./images/looker-look-country-id.png

[looker-api-user-account]: ./images/looker-api-user-account.png
[looker-api-user-keys]: ./images/looker-api-user-keys.png

[looker-api-explorer-gl-request]: ./images/looker-api-explorer-gl-request.png
[looker-api-explorer-gl-response]: ./images/looker-api-explorer-gl-response.png
[looker-api-explorer-riq-request]: ./images/looker-api-explorer-riq-request.png
[looker-api-explorer-riq-response]: ./images/looker-api-explorer-riq-response.png

[looker-api-backend-run]: ./images/looker-api-backend-run.png
[looker-api-backend-test]: ./images/looker-api-backend-test.png