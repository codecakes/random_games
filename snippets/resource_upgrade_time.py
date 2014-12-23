def resources_vs_time(upgrade_cost_increment, num_upgrades):
    """
    num_upgrades: num of upgrades=pairs of the form [current_time, total_resources_generated]
    upgrade_cost_increment:Increase the Upgrade cost each time when increment happens, At the time when upgrade can happen
    total_t: total time since initialization= since beginning
    total_cost: Total resources cost till present time
    total_res: total resources generated
    current_time: time at current iteration.
    current_resource_generated: total resources at hand currently
    time_taken_for_upgrade: time req to reach next upgrade cost
    upgrade_cost: cost of next upgrade (increases by a fixed increment)
    current_res_gen_rate: current resources generation rate (units per sec)
    rate_inc: increase current_res_gen_rate by this increment
    difference of left produce: current_res_gen_rate - upgrade_cost
    """
    rate_inc = 1
    time_taken_for_upgrade = total_t = current_time = current_resource_generated = total_resources_generated = 0
    current_res_gen_rate = upgrade_cost = 1
    res_vs_time = []
    for _ in xrange(num_upgrades):
        #compute current stats
        time_taken_for_upgrade = float(upgrade_cost)/current_res_gen_rate
        #print "time_taken_for_upgrade {} | current_res_gen_rate {} | upgrade_cost {}".format(time_taken_for_upgrade, float(current_res_gen_rate), (upgrade_cost))
        total_t += time_taken_for_upgrade
        total_resources_generated += upgrade_cost
        res_vs_time.append((round(total_t, 11), total_resources_generated))

        #current_time = total_t
        #current_resource_generated = total_resources_generated
        upgrade_cost += upgrade_cost_increment
        current_res_gen_rate += rate_inc
    return res_vs_time

def test():
    """
    Testing code for resources_vs_time
    """
    data1 = resources_vs_time(0.5, 20)
    data2 = resources_vs_time(1.5, 10)
    print data1
    print "\n"
    print data2
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2])

if __name__ == "__main__":
    test()
    #print resources_vs_time(0.5, 20)
