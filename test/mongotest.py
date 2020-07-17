# coding=utf-8
__author__='wygdove'
__time__='2019/5/28 19:53'


import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId


# tianjin dev gis latlng
# conf={"mongoServer":"10.1.234.150:37017","database":"dss001","userName":"dss001user","password":"dss001pwd","bucket":"gisfs"}
# tianjin test gis latlng
# conf={"mongoServer":"10.1.130.26:37017","database":"dss001","userName":"dss001user","password":"dss001pwd","bucket":"gisfs"}
# qinghai dev gis latlng
# conf={"mongoServer":"10.1.234.150:37017","database":"dss001","userName":"dss001user","password":"dss001pwd","bucket":"qhgisfs"}

# tianjin dev mgmt wo
# conf={"mongoServer":"10.1.234.150:37017","database":"dsswo","userName":"dsswouser","password":"dsswopwd","bucket":"dsswofs"}
# tianjin dev mgmt wo his
# conf={"mongoServer":"10.1.234.150:37017","database":"dsswosh","userName":"dsswoshser","password":"ddsswoshpwd","bucket":"dsswohisfs"}

# qinghai dev filefs
# conf={"mongoServer":"10.1.234.150:37017","database":"dss001","userName":"dss001user","password":"dss001pwd","bucket":"fs"}

# local
conf={"mongoServer":"127.0.0.1:37017","database":"quantization","userName":"quantization","password":"okmPL<","bucket":"UserAccount"}


conn=pymongo.MongoClient('mongodb://'+conf["mongoServer"])
db=conn.get_database(conf["database"])
# db.authenticate(conf["userName"],conf["password"])
coll=db.get_collection(conf["bucket"])



# data={"updateTime":1559230170431,"operType":"mod","woId":26707,"woType":"chl-base-mod-social","systemId":"mgmt","updateOperId":"liujw","data":{"houseContractVO":{"updateTime":1559230170030,"channelId":80514,"state":1,"updateOperId":"liujw","contractType":"houselease","createTime":1523343569000,"contractId":5604},"unModifiedVO":{"agentContractId":5603,"channelId":80514,"rewardChannelBankId":12803,"captitalChannelBankId":12804,"channelCode":"A71E17YY","state":1,"houseContractId":5604,"globalChannelCode":"29719711E1X0017","baseCreateTime":1523343569000},"traceId":"4C735E6FED9840D4B8973C49B8989DC5","shopVO":{"updateTime":1559230170030,"openTime":1522512000000,"shopArea":100,"channelId":80514,"state":1,"updateOperId":"liujw","businessArea":100,"createTime":1523343569000},"captitalBankVO":{"acctState":1,"updateTime":1559230170030,"channelId":80514,"acctType":"capital","channelBankId":12804,"updateOperId":"liujw","acctChargebacks":"1","createTime":1523343569000},"baseVO":{"updateTime":1559230170030,"contactPhone":"18237168762","deptId3":"DDEPT008","deptId2":"Z0000973","accessWay":"1","channelId":80514,"channelCode":"A71E17YY","contractBond":1000000000,"admRegCityCode":"0971","channelClass":"cmchl-social","payDepositFlag":0,"deptId1":"Z000QHAI","globalChannelCode":"29719711E1X0017","chlKindName":"专营店","coreFlag":1,"businessCircleType":"无","chlSecondKindId":"200","chlThirdKindId":"210","channelAddress":"1","resAuthType":"","telecomOperatorId":"CM","state":1,"lineType":"BUSI-LINE","busiRegGridCode":None,"updateOperId":"liujw","busiRegName":None,"constructMode":"A","busiRegMicroAreaCode":None,"admRegCode":"A719","chlKindId":"210","channelStarLevel":"1","lineKind":"B-CHANNEL","bindManagerFlag":0,"admRegProvinceCode":"QHAI","businessMode":"D","managerEntityFlag":"0","createTime":1523343569000,"deptId":"DDEPT008","channelName":"渠道类型线条测试-zhangdq","businessCarry":"1","busiRegCode":None,"businessNature":"0","regionType":"1","busiRegProvinceCode":None,"chlFirstKindId":"001","admRegName":"省公司","busiRegCountyCode":None,"busiRegAreaCode":None,"admRegCountyCode":"A719","busiRegCityCode":None,"deptName":"农业发展银行"},"attachList":[],"qualityVO":{"agentIndustryType":"01","registeredCapital":"100000000","btToVatNature":"1","legalEntityFlag":0,"businessLicense":"1","channelId":80514,"businessState":"0","updateTime":1559230170030,"legalCertType":"1","businessServiceScope":"1","legalPhone":"18237168762","legalRepresentative":"1","agentName":"1","updateOperId":"liujw","legalIdno":"1","createTime":1523343569000,"currState":1},"rewardBankVO":{"acctState":1,"acctNo":"1","cityMgrTaxRate":"0","personTaxRate":"0","bankName":"1111111","acctSmsPhone":"18237168762","channelId":80514,"acctType":"reward","updateTime":1559230170030,"issuedInvoiceFlag":"0","channelBankId":12803,"eduTaxRate":"0","acctName":"1","acctNature":"1","updateOperId":"liujw","acctClass":"1","localEduTaxRate":"0","createTime":1523343569000,"branchBankName":"1","valueAddedTaxRate":"0"},"agentContractVO":{"updateTime":1559230170030,"contractEndTime":1525795200000,"contractStartTime":1524672000000,"channelId":80514,"state":1,"updateOperId":"liujw","contractCode":"111","contractType":"authagent","contractName":"11111111111","createTime":1523343569000,"contractId":5603},"workOrderVO":{"woType":"chl-base-mod-social"}},"createTime":1559230170431}
# data={"updateTime":1559230170431,"operType":"mod","woId":26707,"woType":"chl-base-mod-social","systemId":"mgmt","updateOperId":"liujw","data":{"houseContractVO":{"updateTime":1559230170030,"channelId":80514,"state":1,"updateOperId":"liujw","contractType":"houselease","createTime":1523343569000,"contractId":5604},"unModifiedVO":{"agentContractId":5603,"channelId":80514,"rewardChannelBankId":12803,"captitalChannelBankId":12804,"channelCode":"A71E17YY","state":1,"houseContractId":5604,"globalChannelCode":"29719711E1X0017","baseCreateTime":1523343569000},"traceId":"4C735E6FED9840D4B8973C49B8989DC5","shopVO":{"updateTime":1559230170030,"openTime":1522512000000,"shopArea":100,"channelId":80514,"state":1,"updateOperId":"liujw","businessArea":100,"createTime":1523343569000},"captitalBankVO":{"acctState":1,"updateTime":1559230170030,"channelId":80514,"acctType":"capital","channelBankId":12804,"updateOperId":"liujw","acctChargebacks":"1","createTime":1523343569000},"baseVO":{"updateTime":1559230170030,"contactPhone":"18237168762","deptId3":"DDEPT008","deptId2":"Z0000973","accessWay":"1","channelId":80514,"channelCode":"A71E17YY","contractBond":1000000000,"admRegCityCode":"0971","channelClass":"cmchl-social","payDepositFlag":0,"deptId1":"Z000QHAI","globalChannelCode":"29719711E1X0017","chlKindName":"\u4e13\u8425\u5e97","coreFlag":1,"businessCircleType":"\u65e0","chlSecondKindId":"200","chlThirdKindId":"210","channelAddress":"1","resAuthType":"","telecomOperatorId":"CM","state":1,"lineType":"BUSI-LINE","busiRegGridCode":"","updateOperId":"liujw","busiRegName":"\u57ce\u5357\u7247\u533a","constructMode":"A","busiRegMicroAreaCode":"","admRegCode":"A719","chlKindId":"210","channelStarLevel":"1","lineKind":"B-CHANNEL","bindManagerFlag":0,"admRegProvinceCode":"QHAI","businessMode":"D","managerEntityFlag":"0","createTime":1523343569000,"deptId":"DDEPT008","channelName":"\u6e20\u9053\u7c7b\u578b\u7ebf\u6761\u6d4b\u8bd5-zhangdq","businessCarry":"1","busiRegCode":"P71009","businessNature":"0","regionType":"1","busiRegProvinceCode":"QHAI","chlFirstKindId":"001","admRegName":"\u7701\u516c\u53f8","busiRegCountyCode":"A71E","busiRegAreaCode":"P71009","admRegCountyCode":"A719","busiRegCityCode":"0971","deptName":"\u519c\u4e1a\u53d1\u5c55\u94f6\u884c"},"attachList":[],"qualityVO":{"agentIndustryType":"01","registeredCapital":"100000000","btToVatNature":"1","legalEntityFlag":0,"businessLicense":"1","channelId":80514,"businessState":"0","updateTime":1559230170030,"legalCertType":"1","businessServiceScope":"1","legalPhone":"18237168762","legalRepresentative":"1","agentName":"1","updateOperId":"liujw","legalIdno":"1","createTime":1523343569000,"currState":1},"rewardBankVO":{"acctState":1,"acctNo":"1","cityMgrTaxRate":"0","personTaxRate":"0","bankName":"1111111","acctSmsPhone":"18237168762","channelId":80514,"acctType":"reward","updateTime":1559230170030,"issuedInvoiceFlag":"0","channelBankId":12803,"eduTaxRate":"0","acctName":"1","acctNature":"1","updateOperId":"liujw","acctClass":"1","localEduTaxRate":"0","createTime":1523343569000,"branchBankName":"1","valueAddedTaxRate":"0"},"agentContractVO":{"updateTime":1559230170030,"contractEndTime":1525795200000,"contractStartTime":1524672000000,"channelId":80514,"state":1,"updateOperId":"liujw","contractCode":"111","contractType":"authagent","contractName":"11111111111","createTime":1523343569000,"contractId":5603},"workOrderVO":{"woType":"chl-base-mod-social"}},"createTime":1559230170431}

# coll.update_one({"_id":ObjectId(id)},{"$set":data})

# coll.insert({"classCode":"indexFund","className":"指数基金"})

query={}
# query={"_id":ObjectId("5e1d7fd43b7750424eaef071")}
# query={"tYPE":"GIS-GRID"}
# query={"tYPE":"GIS-GRID","cODE":"B1WG0301"}
# query={"tYPE":"GIS-MICRO-GRID"}
# query={"tYPE":"GIS-CHANNEL"}
# query={"tYPE":"GIS-RIVAL"}
# query={"tYPE":"GIS-HOUSING"}
# query={"tYPE":"GIS-BASESTATION"}
# query={"tYPE":"GIS-BASESTATION","bASESTATIONCODE":"8454_17453"}
# query={"nAME":"lalala070401"}

# query={"woId":66402}
# query={"channelCode": "12110123"}
# query={"_id":ObjectId("5943eb264f2d0c5da6aef121")}


# coll.delete_one(query)
# coll.delete_many(query)
data=coll.find(query)
data=json.loads(dumps(data))
print json.dumps(data)



