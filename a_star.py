class AStar():
    def __init__(self, env):
        self.agent_dict = env.agent_dict
        self.admissible_heuristic = env.admissible_heuristic
        self.is_at_goal = env.is_at_goal
        self.get_neighbors = env.get_neighborsz8

    def reconstruct_path(self, history_path, current_path):
        entirety_path = [current_path]

        while current_path in history_path.keys():
            current_path = history_path[current_path]
            entirety_path.append(current_path)

        return entirety_path[::-1]