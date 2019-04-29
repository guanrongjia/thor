# coding=utf8
import json
from dom_action import get_dom_html
from data_action import get_data


def main():
    dom_html = get_dom_html()
    game_data = get_data(dom_html)
    return game_data


if __name__ == '__main__':
    print json.dumps(main(), ensure_ascii=False)
    # {"game_finished": [{"team1": "阿基里斯后备队", "team2": "SBV精英队后备队"}, {"team1": "费耶诺德后备队", "team2": "幸运薛达后备队"}, {"team1": "意大利U15", "team2": "捷克U15"}, {"team1": "亚特兰大", "team2": "乌迪内斯"}, {"team1": "奥斯特桑斯", "team2": "赫尔辛堡"}, {"team1": "松兹瓦尔", "team2": "法尔肯堡"}, {"team1": "哥德堡", "team2": "索尔纳"}, {"team1": "奥雷布洛", "team2": "卡尔马"}, {"team1": "瓦勒伦加", "team2": "奥德格伦兰"}, {"team1": "洛斯查兰特", "team2": "米迪兰特"}, {"team1": "干亚斯堡", "team2": "加拉塔萨雷"}, {"team1": "马拉蒂亚体育", "team2": "卡斯帕萨"}, {"team1": "普罗夫迪夫博特夫", "team2": "索非亚中央陆军"}, {"team1": "韦恩", "team2": "凯泽斯劳滕"}, {"team1": "奥斯达", "team2": "诺尔比"}, {"team1": "布莱尼B队", "team2": "斯达约珀兰"}, {"team1": "B73斯萊格思B队", "team2": "哈斯莱乌FC"}, {"team1": "维米斯B", "team2": "帕尔努瓦夫鲁"}, {"team1": "卡达西亚SC", "team2": "阿尔阿希德"}, {"team1": "维德兹尔斯", "team2": "维尔提斯"}, {"team1": "佛罗亚", "team2": "特罗姆瑟B队"}, {"team1": "威尔郡U21", "team2": "科特赖克U21"}, {"team1": "安特卫普U21", "team2": "布鲁日U21"}, {"team1": "欧本U21", "team2": "圣图尔登U21"}, {"team1": "奥斯坦德U21", "team2": "华斯兰比华伦U21"}, {"team1": "标准列日U21", "team2": "亨克U21"}, {"team1": "洛格伦U21", "team2": "真特U21"}, {"team1": "乌拉圭沙滩足球队", "team2": "厄瓜多尔沙滩足球队"}, {"team1": "诺霍斯B队", "team2": "积奥维克"}, {"team1": "CNEPS", "team2": "迪雅宝罗斯"}, {"team1": "泽沃勒", "team2": "格罗宁根"}, {"team1": "阿贾克斯青年队", "team2": "特温特"}, {"team1": "克卢日", "team2": "维托鲁康斯坦萨"}, {"team1": "特拉维夫叶胡达", "team2": "海法马卡比"}, {"team1": "EB斯特莱马", "team2": "福格拉夫约杜尔"}, {"team1": "色格拉布鲁日U21", "team2": "安德莱赫特U21"}, {"team1": "南安普顿U23", "team2": "桑德兰U23"}, {"team1": "热刺U23", "team2": "德比郡U23"}, {"team1": "西汉姆联U23", "team2": "埃弗顿U23"}, {"team1": "曼城U23", "team2": "斯旺西U23"}, {"team1": "阿斯顿维拉U23", "team2": "西布朗维奇U23"}, {"team1": "利兹联U23", "team2": "考文垂U23"}, {"team1": "尤尼奥哈U20", "team2": "新奥里藏特RS青年队"}, {"team1": "广士云格B队", "team2": "布鲁蒙德尔"}, {"team1": "卡斯尔斯女足", "team2": "维拉诺瓦女足"}, {"team1": "科尔公园联合", "team2": "克鲁姆林联"}, {"team1": "埃森", "team2": "华登舒特"}, {"team1": "杜伊斯堡", "team2": "比勒菲尔德"}, {"team1": "圣德尔模", "team2": "卡塞罗斯学生队"}, {"team1": "菲尼斯皮拉尔", "team2": "弗朗德里亚"}, {"team1": "萨卡兹斯帕斯", "team2": "阿卡苏索"}, {"team1": "拉费雷尔", "team2": "卡纽埃拉斯"}, {"team1": "霍舍姆", "team2": "海沃德希思镇"}, {"team1": "史塔夫流浪", "team2": "卢莎奥林"}, {"team1": "努瓦克肖特国王", "team2": "ASAC康戈德"}, {"team1": "圣米格尔", "team2": "巴拉卡斯中央队"}, {"team1": "洛里昂", "team2": "欧塞尔"}, {"team1": "德利城", "team2": "波希米亚人"}, {"team1": "都柏林大学", "team2": "斯莱戈流浪"}, {"team1": "沃特福德联队", "team2": "登克尔克"}, {"team1": "科克城", "team2": "费恩夏普"}, {"team1": "哈士汀联", "team2": "阿舒福特"}, {"team1": "科尔尼", "team2": "南港队"}, {"team1": "巴西沙滩足球队", "team2": "哥伦比亚沙滩足球队"}, {"team1": "佛罗伦萨", "team2": "森索罗"}, {"team1": "皇家贝蒂斯", "team2": "西班牙人"}, {"team1": "沙姆洛克流浪", "team2": "圣帕特里克"}, {"team1": "哈撒那", "team2": "泽姆"}, {"team1": "格伦杜兰女足", "team2": "精梳娱乐女足"}, {"team1": "凤凰重生", "team2": "西雅图音速后备队"}, {"team1": "萨莫拉FC", "team2": "塔赤雷"}, {"team1": "艾斯图第安特U20", "team2": "拉尼罗斯瓜纳雷U20"}, {"team1": "泰格雷", "team2": "圣塔菲联"}, {"team1": "卡瓦立尔", "team2": "普莱森特法山"}, {"team1": "科里蒂巴", "team2": "庞特普雷塔"}, {"team1": "茨高", "team2": "锡帕基拉老虎"}, {"team1": "拉斯帕雷加斯体育", "team2": "康赛普森吉姆纳西亚"}, {"team1": "圣十字", "team2": "特利茲"}, {"team1": "CA萨尔内斯", "team2": "乌贝兰迪亚"}, {"team1": "国民AC MG", "team2": "科英布拉体育"}, {"team1": "亚松森瓜拉尼", "team2": "桑坦尼体育会"}, {"team1": "SV维斯塔", "team2": "CRKSV"}, {"team1": "拉普拉塔体操", "team2": "防卫者"}, {"team1": "德芬", "team2": "马卡拉"}, {"team1": "佩雷拉", "team2": "巴瑞库拉"}, {"team1": "波特莫尔联", "team2": "沃特豪斯"}, {"team1": "洛杉矶银河B队", "team2": "拉斯维加斯光"}, {"team1": "北部吉隆勇士", "team2": "萨巴拉斯"}, {"team1": "卡雅FC", "team2": "老挝丰田"}, {"team1": "上海申鑫", "team2": "青岛中能"}, {"team1": "吉林百嘉", "team2": "青岛黄海"}, {"team1": "辽宁沈阳宏远", "team2": "北京人和"}, {"team1": "PSM马卡萨", "team2": "内政联队"}, {"team1": "马都拉联", "team2": "帕尔斯巴亚"}, {"team1": "伊朗女足U19", "team2": "黎巴嫩女足U19"}, {"team1": "澳洲女足U19", "team2": "乌兹别克女足U19"}, {"team1": "天津泰达亿利", "team2": "淄博蹴鞠"}, {"team1": "胡占德", "team2": "阿尔廷阿西尔"}, {"team1": "蒙纳斯堤", "team2": "加贝斯"}, {"team1": "埃尔夫斯堡U21", "team2": "卡尔马U21"}, {"team1": "锆石", "team2": "雅基耶"}, {"team1": "图伦努库斯", "team2": "拉什乳业"}, {"team1": "和富大埔", "team2": "四二五体育会"}, {"team1": "CS哈曼利弗", "team2": "斯法克斯"}, {"team1": "韩国女足U19", "team2": "越南女足U19"}, {"team1": "缅甸女足U19", "team2": "尼泊尔女足U19"}, {"team1": "斯霍拉", "team2": "欧鲁巴赫"}, {"team1": "乌尔米耶", "team2": "马拉云"}, {"team1": "库内巴博勒", "team2": "卡隆阿瓦"}, {"team1": "马赫沙尔", "team2": "法加尔瑟帕斯"}, {"team1": "斯兰泽游牧者", "team2": "塔比之"}, {"team1": "厄尔布尔士", "team2": "高尔高赫"}, {"team1": "克尔曼", "team2": "巴德兰德黑兰"}, {"team1": "沙禾达利亚拉克", "team2": "波斯波利斯帕克达什特"}, {"team1": "德咸科", "team2": "卡威帕"}, {"team1": "EGS加夫萨", "team2": "沙拜"}, {"team1": "班南特斯B队", "team2": "塞万青年"}, {"team1": "查巴垒", "team2": "瓦沙姆"}, {"team1": "泰坦", "team2": "阿巴哈尼"}, {"team1": "伊奥华女足", "team2": "切尔西女足"}, {"team1": "拉尼奇1923", "team2": "兹拉蒂博尔"}, {"team1": "JSM贝贾亚", "team2": "伊尤马"}, {"team1": "哥登堡U21", "team2": "咸史泰斯U21"}, {"team1": "亚吉拉安曼", "team2": "拿杰玛"}, {"team1": "厄瓜多尔沙滩足球队", "team2": "哥伦比亚沙滩足球队"}, {"team1": "明斯克迪拿摩", "team2": "维特布斯克火车头"}, {"team1": "拉巴特皇家武装", "team2": "卡萨布兰卡维达德"}, {"team1": "戴戈福斯U21", "team2": "IFK诺科平U21"}, {"team1": "韦斯特罗斯U21", "team2": "奥雷布洛U21"}, {"team1": "维霍维纳", "team2": "维克梅济日奇"}, {"team1": "胡林斯巴达克", "team2": "奥特罗科维斯"}, {"team1": "拉赫蒂", "team2": "VPS瓦萨"}, {"team1": "未来之星", "team2": "艾德瀚德"}, {"team1": "伊斯梅利", "team2": "哈伊赫多"}, {"team1": "史莫哈", "team2": "艾尔格纳"}, {"team1": "伊蒂哈德阿勒颇", "team2": "阿尔科威特"}, {"team1": "诺积姆", "team2": "艾伯哈"}, {"team1": "卡利杰", "team2": "阿尔泰"}, {"team1": "索尔美洲队后备队", "team2": "路昆奴体育后备队"}, {"team1": "保塞勒蒙", "team2": "加贝申"}, {"team1": "艾拉斯克特B队", "team2": "卡磐B队"}, {"team1": "阿根廷沙滩足球队", "team2": "委内瑞拉沙滩足球队"}, {"team1": "巴拉圭沙滩足球队", "team2": "秘鲁沙滩足球队"}, {"team1": "帕丘卡女足", "team2": "阿特拉斯女足"}, {"team1": "堤格雷斯女足", "team2": "普埃布拉女足"}, {"team1": "莫兰德城", "team2": "圣奥尔本斯圣特斯"}, {"team1": "华勒比市", "team2": "布伦瑞克城"}, {"team1": "金马阿坝", "team2": "锡达马"}, {"team1": "阿达玛市", "team2": "埃塞俄比亚文和"}, {"team1": "佐伯阿汉", "team2": "塞柏"}, {"team1": "圣格鲁吉", "team2": "默克莱凯内马"}], "game_in_progress": [{"current_score": "1-2", "team1": "索莱尔FC", "team2": "龙队"}, {"current_score": "1-0", "team1": "CS卡拉奥华大学", "team2": "舍佩斯"}, {"current_score": "0-1", "team1": "加巴尼亚", "team2": "GKS卡托威斯"}, {"current_score": "1-3", "team1": "图兹拉市", "team2": "兹维耶达"}, {"current_score": "0-0", "team1": "马卡比伊罗尼斯德洛特", "team2": "贝塔尔拉马特甘"}, {"current_score": "1-1", "team1": "沙维斯B队", "team2": "吉维森特"}, {"current_score": "2-1", "team1": "英特土尔库", "team2": "赫尔辛基"}, {"current_score": "0-0", "team1": "HIFK足球", "team2": "洪卡"}, {"current_score": "0-1", "team1": "阿米蒂FC", "team2": "非洲促销足"}, {"current_score": "0-1", "team1": "迪哈夫拉", "team2": "迪拜阿赫利"}, {"current_score": "1-0", "team1": "波尔图U19", "team2": "切尔西U19"}, {"current_score": "0-0", "team1": "希拉尔", "team2": "塔亚文"}, {"current_score": "2-0", "team1": "萨比利斯", "team2": "索斯诺维克"}, {"current_score": "0-2", "team1": "卡拉比克体育", "team2": "根克勒比利吉"}, {"current_score": "1-0", "team1": "埃斯基谢希尔体育", "team2": "阿菲永士邦"}, {"current_score": "0-0", "team1": "玛基亚", "team2": "苏维克"}, {"current_score": "2-0", "team1": "乌斯季", "team2": "帕尔杜比斯"}, {"current_score": "1-0", "team1": "阿卡夏普尔", "team2": "迪克瓦夏普尔"}, {"current_score": "0-0", "team1": "雷霍沃特夏普尔", "team2": "柏纳洛德夏普尔"}, {"current_score": "0-0", "team1": "阿基纳扎力", "team2": "里雄莱锡安夏普尔"}, {"current_score": "1-0", "team1": "哈萨隆", "team2": "埃克萨夏普尔"}, {"current_score": "1-2", "team1": "諾德斯特蘭德", "team2": "莫尔德B队"}, {"current_score": "2-2", "team1": "史特连希咸", "team2": "雷黑姆B队"}, {"current_score": "1-0", "team1": "玛达", "team2": "史达B"}, {"current_score": "0-0", "team1": "莫斯科斯巴达", "team2": "喀山鲁宾"}, {"current_score": "0-1", "team1": "都灵青年队", "team2": "切沃青年队"}, {"current_score": "0-0", "team1": "阿高斯后备队", "team2": "罗达JC后备队"}, {"current_score": "0-0", "team1": "川迪后备队", "team2": "海牙后备队"}, {"current_score": "0-0", "team1": "坎布尔后备队", "team2": "迪加史卓普后备队"}, {"current_score": "0-0", "team1": "海伦维恩后备队", "team2": "赫尔蒙德后备队"}, {"current_score": "0-0", "team1": "多德勒支后备队", "team2": "FC埃因霍温后备队"}, {"current_score": "0-0", "team1": "荷华高斯后备队", "team2": "埃曼后备队"}, {"current_score": "0-0", "team1": "岡比亞武装部队", "team2": "皇家班珠尔"}, {"current_score": "0-0", "team1": "阿尔美", "team2": "ASC斯尼姆"}, {"current_score": "1-1", "team1": "奥伦堡加索维克", "team2": "图拉兵工厂"}, {"current_score": "2-0", "team1": "基辅阿森纳", "team2": "德斯纳切尼赫夫"}, {"current_score": "0-1", "team1": "加拉波沃", "team2": "卢多戈雷茨B队"}, {"current_score": "1-4", "team1": "哥德堡大力士U21", "team2": "特利堡U21"}, {"current_score": "5-3", "team1": "飞燕诺U19", "team2": "阿贾克斯U19"}, {"current_score": "3-2", "team1": "斯巴达萨普斯堡B队", "team2": "斯塔贝克B队"}, {"current_score": "1-0", "team1": "慕尼斯帕尔体育后备队", "team2": "阿亚库乔后备队"}, {"current_score": "2-2", "team1": "索非亚斯拉维亚", "team2": "普罗夫迪夫火车头"}]}