# DeepMasterPrint2

![example pic](images/example.png)
This repository contains the code for the paper _[Diversity and Novelty MasterPrints: Generating Multiple DeepMasterPrints for Increased User Coverage](https://arxiv.org/pdf/2209.04909.pdf)_


## Requirements
Set up the environment (we use `python 3.7` for this codebase):
```
python -m pip install -r requirements.txt
```

For using the code, many of the paths route to local code utils files and datasets (i.e. the wrapper Verifinger code [`sub_verifinger.py`](Verifinger_Custom_Code/sub_verifinger.py)). Please remember to change these paths to match your own local path. 

## Usage
- For a print generator model, run [`Print_Autoencoder.ipynb`](Print_Autoencoder.ipynb)
- For a matching model, run [`Print_Multiclassifier_Trainer.ipynb`](Print_Multiclassifier_Trainer.ipynb)
- To run the experiements in the paper, run [`SP Experiment (PAPER).ipynb`](SP%20Experiment%20(PAPER).ipynb)
- To run test experiments, run [`SP Exp - Test Dataset Coverage.ipynb`](SP%20Exp%20-%20Test%20Dataset%20Coverage.ipynb)
- To visualize experiment results, run [`Show_Archive.ipynb`](Show_Archive.ipynb)


## OUTPUT DESCRIPTION

### Print Archive
`[BINARY USER CHROMOSOME]:[Z VECTOR REPRESENTATION]\n~~~\n`
`[BINARY USER CHROMOSOME]` - which users were considered matched based on index (i.e. 01011 means users indexed at 1,3, and 4 matched the print)
`[Z VECTOR REPRESENTATION]` - the vector that is passed to the generator model to recreate the print that made the match (size 100 vector)
'~~~' - separates each archive

EXAMPLE:
```
000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000101:-1.916533153699789,1.9519441294254887,-2.8743252190614204,-0.36298462759511463,-4.292081166868176,-0.36051428508456107,2.452029917240232,2.2809535545004254,-1.1153275455291682,1.9472607723156556,-1.7404678497066617,2.4521793582236553,-0.544386649222518,0.10903939164172712,-2.4435406044858903,1.045524958128742,-3.7482639189880134,-0.9059521063142969,1.5746879674702086,-0.0957672170773807,2.7313473801968473,-1.3850818984616797,2.1394738613938293,2.2949567409389546,3.209020091564548,-1.0482971812571233,-1.7794072596689505,-2.6406414181238977,-2.510785292336254,6.390992983865887,3.47264130251856,-0.41851924060904755,0.3162830949041101,-0.40192158301514636,1.5785416854562127,2.0769120990958316,2.277363204516438,-0.11966112358969433,-1.3548975272788855,-1.8827406536793985,-2.987194960361814,0.8269256721752659,-1.9870859886940695,2.4637826775998866,0.9407007559918028,-3.2307118053925223,-2.167681130126757,-0.8563562285045749,4.5272068758006885,-1.334781931909737,1.6201928911387267,-5.048491811953651,-2.1815671876174765,5.487640176133895,-4.976405020383494,-1.7825272798147465,1.9994153766903662,0.28399751551415336,7.236647637804982,-2.925995031760298,1.7370390079399227,1.0342176516386805,2.2130768575898014,-0.8972380994069225,2.6761498114521314,-0.9073613711866186,-2.5706123753004624,2.420933719363555,0.6482563638036358,-2.4653805609174326,-1.852986864081839,-0.9815290321940904,-3.64418252863636,-0.31571908158320794,0.17065255811330132,2.2516119358911135,-3.6952637142464666,0.6323548095841632,-2.731984990706609,3.636633660012249,0.1476257045110915,2.8097238788255,0.7991411494267364,-0.5845040747241759,-4.243521659332214,-1.4907422362167178,3.5741712316601357,0.8099135983439918,-0.42049094159113914,-0.4670134345661672,-3.8724729668230875,5.339967552688013,-0.5630499111454552,0.37698423065422226,-0.4453042115200903,-1.2453519209247519,-4.078612797994481,2.78399212242783,1.5439549390316845,-6.433698067991634
~ ~ ~
000000000000000...
```

### Coverage Report
```
**EXPERIMENT** - the experiment type this was tested on [DeepMasterPrint, Random, Novelty, Diversity]
**DATASET** - the dataset used
**FMR** - the false match rate used in the experiment to matching users
**TTYPE** - training, testing, or full dataset split
**CLASSIFIER** - the matching classifier used for the experiment [Verifinger, MLC]
**COVERAGE** - the percentage of user match coverages of the archives in each trial ordered from most to least coverage
```

*EXAMPLE*:
```
EXPERIMENT:DMP
DATASET:CAPACITIVE
FMR:0.1
TTYPE:train
CLASSIFIER:MLC
COVERAGE:[0.005555555555555556, 0.005555555555555556, 0.002777777777777778, 0.002777777777777778, 0.002777777777777778, 0.002777777777777778, 0.0, 0.0, 0.0, 0.0]

```

## Notes
To run this code fully you must download the Verifinger framework software. Please see the _[README](Verifinger_Custom_Code/README.md)_ in the `Verifinger_Custom_Code` folder for more information.

Kindly be informed that the dataset employed in this code repository is not included due to copyright and privacy restrictions. However, we have indicated the specific dataset used (CAPACITIVE, OPTICAL, NIST)(see our [previous work](https://arxiv.org/pdf/1705.07386.pdf) for detail), enabling you to source it from the designated provider. Please make sure to adhere to all copyright and usage regulations when obtaining and utilizing the dataset.


## BibTeX
```
@inproceedings{charity2022diversity,
  title={Diversity and Novelty MasterPrints: Generating Multiple DeepMasterPrints for Increased User Coverage},
  author={Charity, M and Memon, Nasir and Jiang, Zehua and Sen, Abhi and Togelius, Julian},
  booktitle={2022 International Conference of the Biometrics Special Interest Group (BIOSIG)},
  pages={1--4},
  year={2022},
  organization={IEEE}
}
```