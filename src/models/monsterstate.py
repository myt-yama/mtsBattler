class MonsterState:
    """
    モンスター戦闘状況

    Attributes
    ----------
    player       : int
        1P or 2P
    team         : str
        チーム名
    name         : str
        名前
    hp           : int
        HP
    charge       : int
        チャージ数
    """
    @classmethod
    def get_monster_state_param(cls):
        return [
            'player',
            'team',
            'hp',
            'charge'
        ]

    def set_monster(self, player, monster):
        self.player = player
        self.team = monster.team
        self.name = monster.name
        self.hp = monster.hp
        self.charge = 0

    def set_monster_state(self, state):
        self.player = state['player']
        self.team = state['team']
        self.name = state['name']
        self.hp = state['hp']
        self.charge = state['charge']




