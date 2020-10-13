# secretory-cleft-ibamr

This project uses IBAMR and VisIt to simulate secretory clefts in CD8+ T-Cells.

## Installation

### Installing Docker

#### Windows, Linux, MacOS (Binary Package)
https://docs.docker.com/get-docker/

#### MacOS
Recommended install with cask: ```brew cask install docker```

### Pulling Docker Image from Docker Hub
```
docker pull ericlee3141/ibamr_secretory_cleft:latest
docker image ls # Note <IMAGE ID>
docker tag <IMAGE ID> <YOUR IMAGE NAME>:latest
docker rmi ericlee3141/ibamr_secretory_cleft:latest
docker run -n <YOUR CONTAINER NAME> -it <YOUR IMAGE NAME>
```

## Usage

### Running Simulation
```
docker start -i <YOUR CONTAINER NAME>
cd /usr/test/sfw/ibamr/ibamr-objs-opt/examples/IB/explicit/test
./main2d input2d
exit
```
### Exporting Simulation Data
```
cd /PATH/TO/FOLDER
docker cp <YOUR CONTAINER NAME>:/usr/test/sfw/ibamr/ibamr-objs-opt/examples/IB/explicit/ex3/viz_IB2d/ .
```

## Visualizing Data

### Installing VisIt (Binary Package)
https://wci.llnl.gov/simulation/computer-codes/visit/executables

(Include Screenshots here)

Open > viz_IB2d > lag_data.visit

Add > Subset > fila_256_mesh

Open > viz_IB2d > dumps.visit

dumps.visit:Subset - levels > Delete

Add > Pseudocolor > P

dumps.visit:Pseudocolor - P > Pseudocolor > Opacity > Constant > ~20%

Draw

<!--
# markdown tutorial
# Docker cp
# Add them as collab 
# Add docker link somehow???
# Make the markdown file like a tutorial
# Make movie recordings
# Organize simulation files 
-->