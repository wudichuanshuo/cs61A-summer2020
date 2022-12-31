def say_scores(last_leader=None):
    def announce_lead_changes(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print(1)
        return say_scores(leader)
    return announce_lead_changes
    