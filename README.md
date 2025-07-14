# 🚗 Vehiculometric Adjudicator  
*A Perspicacious Algorithmic Arbiter of Automotive Appropriateness*

## Prolegomenon

Behold an earnest undertaking in the realm of algorithmic discernment — a machine learning–augmented artefact that prognosticates the **acceptability of a vehicle** based upon multifarious categorical criteria. Designed with a blend of computational rigour and aesthetic sensibility, this web application allows users to input vehicular attributes and receive a calibrated judgment on its overall acceptability, as perceived through the algorithmic gaze of various classifiers.

## Functional Overview

At its core, this adjudicator digests the following vehicular determinants:
- **Buying Price** (`low`, `med`, `high`, `vhigh`)
- **Maintenance Cost**
- **Number of Doors**
- **Seating Capacity**
- **Luggage Boot Size**
- **Safety Rating**

Upon ingestion of the above, it employs one of several classifier algorithms to infer the **acceptability** of the vehicle:  
`Unaccurate`, `Accurate`, `Good`, or `Very Good` — each determined through data-trained models with metric-backed veracity.

## Algorithms of Adjudication

The backend apparatus facilitates comparative predictions using:
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Support Vector Classifier (SVC)**

Each model returns performance metrics including:
- Accuracy  
- Precision  
- Recall  
- F1 Score  

so that the user may discern not just what was predicted, but how well the model behaves.

## Data Provenance

The dataset, a canonical corpus widely cited in machine learning pedagogy, was graciously obtained from [Marco Bohanec](https://file.biolab.si/biolab/app/hint/car_dataset.html). 

Full citation:

> Bohanec, M., & Rajkovič, V. (1995). **CAR Evaluation Database**.  
> University of California, Irvine - UCI Machine Learning Repository.

This dataset encodes expert knowledge collected from hierarchical decision-making models intended for vehicle evaluation.

## Deployment & Usage

> This application currently resides in the local dominion and is not yet deployed in the digital ether. To instantiate it on your machine:

1. Clone this repository:
   ```bash
   git clone https://github.com/har5hdeep5harma/Vehiculometric-Adjudicator.git
   cd Vehiculometric-Adjudicator
   ```

2. Install the minimal dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
3. Launch the Flask application:
    ```bash
    python main.py
    ```

4. Visit http://localhost:5000 to engage with the arbiter.

## Authorial Note
This project was humbly conceived and constructed by Harshdeep Sharma, in quiet reverence to the elegance of logic and the marvel of machine learning.

"Woven with code and contemplation — an ode to discernment through data."

## License
This project is conceived solely for academic and demonstrative purposes. Redistribution, in part or whole, is prohibited without express permission.
