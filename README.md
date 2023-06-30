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
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#possible-enhancements">Possible Enhancements</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>
<!-- </details> -->

---

<!-- ABOUT THE PROJECT -->

## About The Project

This project is created to showcase how we can `Looker API` to extract information from `Looker` for processing outside of `Looker` environment.

The following are some of the requirements:

- Extract the data information of a particular `Looker` looker view

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- Setup -->

## Setup

Base on the requirements, the following components are required to be setup:

- `BigQuery` - xxxx
- `Looker` - xxxx
- `Looker API` - xxxx
- `Python Dependencies` - xxxx

<p align="right">(<a href="#top">back to top</a>)</p>

### BigQuery

<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

### Looker

<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

### Looker API

<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

### Python Dependencies

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
<br/>

```python
```
<p align="right">(<a href="#top">back to top</a>)</p>

### City Look
This task make use of the `Looker API` to retrieve the data from the city look specify by the *look id* and filter them accordingly to the *country* provided<br/>
<br/>

```python
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
    **Output** <br/>

    | ![cloud-composer-local-output][cloud-composer-local-output] | 
    |:--:| 
    | *Cloud Composer Local Run Output* |

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- Challenges -->
## Challenges

The following are some challenges encountered:
- XXXXXXX
<p align="right">(<a href="#top">back to top</a>)</p>

### Challenge #1: XXXXXXX

**Observations**

<br/>

**Resolution**

<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- Enhancements -->
## Possible Enhancements

- [ ] XXXXXXXXXXX

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Readme Template][template-resource]

<p align="right">(<a href="#top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[template-resource]: https://github.com/othneildrew/Best-README-Template/blob/master/README.md

<!-- | ![looker-api-explorer-application][looker-api-explorer-application] | 
|:--:| 
| *Looker API Explorer* | -->