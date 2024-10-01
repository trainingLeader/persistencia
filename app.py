
import modules.utils.core as cf
if __name__ == '__main__':
    campus={
        'campers':{}
    }
    cf.MY_DATABASE='data/campus.json'
    cf.checkFile(campus)
    # camper = {
    #     'idx' : str(len(campus.get('campers'))+1).zfill(3),
    #     'nombre':'Carlos'
    # }
    camper = {
        'idx' : '002',
        'nombre':'Luis enrique'
    }
    # campus.get('campers').update({camper['idx']:camper})
    cf.AddData('campers', {camper.get('idx'):camper})
    # cf.AddData(campus.get('campers').get('001').get('nombre'),'Pepito perez')
    # print(campus)
    cf.delData('campers', '002', campus)
    print(campus)