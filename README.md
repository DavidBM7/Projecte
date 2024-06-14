Explicació:
Abans d’això vos mostraré com instal·lar diferents versions de python, perquè a vegades en necessitem una millor o tornar a una versió antiga: 
sudo apt install python3.11 o sudo apt install python3.9
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 2 
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
sudo update-alternatives --config python i elegirem la versió que volem per defecte.
Quan ja tenim la versió que volem per defecte, haurem d’instal·lar totes les llibreries necessàries: sudo apt install python3-virtualenv python3-pip
Ara ens posarem al directori on volem crear l’entorn virtual: cd /home/cicles/ao/python
Ara crearem l’entorn virtual: virtualenv epython1
I després l’activarem: source epython1/bin/activate
Dins l’entorn, instal·larem tot els paquets que necessitem:
Llibreria matplotlib:  pip install matplotlib==versió
Fent: pip freeze, veurem les llibreries i les versions instal·lades.
Si vull desactivar un entorn virtual faré: deactivate
En resum, les ordres que es faran són: virtualenv NomAlumne && source NomAlumne/bin/activate
Baixarem el codi font de github:
sudo git clone url (aquesta url és la del teu repositori)
Prepararem l’entorn de feina:
pip install -r requirements.txt
Executarem el codi
python3 NomProgramaPrincipal
