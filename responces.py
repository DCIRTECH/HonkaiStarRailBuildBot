

def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "clara":
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/clara-team-guide/\n\nbuild optimization: ' \
               'https://genshin.gg/star-rail/characters/clara/'
    elif p_message == 'jing yuan' or p_message == 'jingyuan' or p_message == 'jing':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/jingyuan-team-guide/\n\nbuild optimization:' \
               'https://genshin.gg/star-rail/characters/jingyuan/'
    elif p_message == 'silverwolf' or p_message == 'silver wolf' or p_message == 'sw':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/silver-wolf-team-guide/\n\n' \
               'build optimization: https://genshin.gg/star-rail/characters/silverwolf/'
    elif p_message == 'march 7th' or p_message == 'march' or p_message == 'm7' or p_message == 'march7th':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/march7th-team-guide/\n\n' \
               'build optimization: https://genshin.gg/star-rail/characters/march7th/'
    elif p_message == 'trailblazer' or p_message == 'tb':
        return 'fire team comps: https://genshinlab.com/honkai-star-rail-team/trailblazer-fire-team-guide/\n' \
               'fire optimization: https://genshin.gg/star-rail/characters/trailblazer(fire)/\n\n\n' \
               'physical team comps: https://genshinlab.com/honkai-star-rail-team/trailblazer-physical-team-guide/\n'\
               'physical optimization: https://genshin.gg/star-rail/characters/trailblazer(physical)/'
    elif p_message == 'ftrailblazer' or p_message == 'firetrailblazer' or p_message == 'ftb':
        return 'fire team comps: https://genshinlab.com/honkai-star-rail-team/trailblazer-fire-team-guide/\n\n' \
               'fire optimization: https://genshin.gg/star-rail/characters/trailblazer(fire)/'
    elif p_message == 'ptrailblazer' or p_message == 'physicaltrailblazer' or p_message == 'ptb' or \
            p_message == 'phystrailblazer':
        return 'physical team comps: https://genshinlab.com/honkai-star-rail-team/trailblazer-physical-team-guide/\n\n'\
               'physical optimization: https://genshin.gg/star-rail/characters/trailblazer(physical)/'
    elif p_message == 'danheng' or p_message == 'dan heng' or p_message == 'dan':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/danheng-team-guide/\n\n' \
               'optimization: https://genshin.gg/star-rail/characters/danheng/'
    elif p_message == 'himeko':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/himeko-team-guide/\n\n' \
               'optimization: https://genshin.gg/star-rail/characters/himeko/'
    elif p_message == 'asta':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/asta-team-guide/\n\n' \
               'optimization: https://genshin.gg/star-rail/characters/asta/'
    elif p_message == 'arlan':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/arlan-team-guide/\n\n' \
               'optimization: https://genshin.gg/star-rail/characters/arlan/'
    elif p_message == 'seele':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/seele-team-guide/\n\n' \
               'optimization: https://genshin.gg/star-rail/characters/seele/'
    elif p_message == 'natasha' or p_message == 'nat':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/natasha-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/natasha/'
    elif p_message == 'pela':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/pela-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/pela/'
    elif p_message == 'hook':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/hook-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/hook/'
    elif p_message == 'serval':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/serval-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/serval/'
    elif p_message == 'qingque' or p_message == 'qing':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/qingque-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/qingque/'
    elif p_message == 'herta':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/herta-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/herta/'
    elif p_message == 'tingyun' or 'ting':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/tingyun-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/tingyun/'
    elif p_message == 'sushang' or 'sus':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/sushang-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/sushang/'
    elif p_message == 'bronya':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/bronya-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/bronya/'
    elif p_message == 'gepard':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/gepard-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/gepard/'
    elif p_message == 'bailu':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/bailu-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/bailu/'
    elif p_message == 'yanqing':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/yanqing-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/yanqing/'
    elif p_message == 'welt':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/welt-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/welt/'
    elif p_message == 'sampo':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/tingyun-team-guide/\n\n'\
               'optimization: https://genshin.gg/star-rail/characters/sampo/'
    elif p_message == 'luocha':
        return 'team comps: https://genshinlab.com/honkai-star-rail-team/luocha-team-guide/\n\n'\
               'optimization: coming soon'
    elif p_message == 'data':
        return 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQLKk4LzAE2EBo_Lksutbi6X6HIUW_wqo7iL_KDkC_m95FSqqdQ9F9PVFYsu03HNODAPFNRG13wpsdX/pubhtml'
    elif p_message == 'help':
        return 'you can get builds and team comps by typing ?<character name>\n'\
               'example: ?physicaltrailblazer\n'\
               'you can also have very detailed, community updated information by using the command ?data\n'
