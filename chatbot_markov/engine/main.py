import jsonldParser as jp

def main():
    ##
    # ここにいくつかの処理(WebsocketからのJSON-LD取得 等)
    ##

    # JSON-LD読み込み
    # (firstMorning.jsonld,morning.jsonld,noon.jsonld,night.jsonld,result.jsonld,
    # myMessageOnChat.jsonld,theirMessageOnChat.jsonld)
    jp.loadJsonld('firstMorning.jsonld')

    # フェーズの取得
    print(jp.getPhase())

    # キャラデータ取得全員分
    charaData = jp.getCharacterData()
    print(charaData)

    # 自分のデータ取得
    for x in charaData:
        if jp.isMineCharacter(x):
            myData = x
            break

    print(myData)
    # キャラID取得
    print(jp.getCharacterId(myData))

    # キャラ名取得
    print(jp.getCharacterName(myData))

    # キャラステータス取得
    print(jp.getCharacterStatus(myData))

    # isMine取得
    print(jp.isMineCharacter(myData))

    # 役職取得
    roleData = jp.getRoleData()
    print(roleData)

    # 自分の役職データ取得
    for x in roleData:
        if jp.isMineRole(x):
            myRoleData = x
            break

    # 役職名取得
    print(jp.getRoleName(myRoleData))

    jp.loadJsonld('myMessageOnChat.jsonld')
    text = jp.getChatMessage()
    print(text)

    

if __name__ == "__main__":
    main()
