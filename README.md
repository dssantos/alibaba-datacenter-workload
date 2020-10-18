# Alibaba Datacenter Workload Analysis


## Como usar

1. Clone o repositório
2. Crie um virtualenv
3. Ative o virtualenv
4. Instale as dependências
5. Baixe o conjunto de dados (1,7 GB)
6. Descompacte o arquivo
7. Execute o script para separar as maquinas
8. Execute o notebook

```console
git clone https://github.com/dssantos/alibaba-datacenter-workload.git alibaba
cd alibaba
python -m venv .alibaba
source .alibaba/bin/activate
pip install -r requirements.txt
wget http://clusterdata2018pubcn.oss-cn-beijing.aliyuncs.com/machine_usage.tar.gz
tar -zxvf machine_usage.tar.gz
python split_machines.py
jupyter notebook