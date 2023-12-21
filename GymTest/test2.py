import gym

class SimpleAgent:
    def __init__(self, env):
        pass
    
    def decide(self, observation): # 根据给定的观测进行决策，采取动作
        '''
        observation: 观测值,在MountainCar-v0这个例子中，是一个2元素的列表，对应小车的位置和速度
        '''
        position, velocity = observation
        lb = min(-0.09 * (position + 0.25) ** 2 + 0.03,
                0.3 * (position + 0.9) ** 4 - 0.008)
        ub = -0.07 * (position + 0.38) ** 2 + 0.07
        if lb < velocity < ub:
            action = 2 # 右加速
        else:
            action = 0 # 左加速
        return action # 返回动作

    def learn(self, *args): # 学习
        pass
    
def play(env, agent, render=False, train=False):
    '''
    env: 环境类
    agent: 智能体类
    render: 是否图形化显示
    train: 是否训练智能体，训练时为True,测试时为False
    '''
    episode_reward = 0. # 记录回合总奖励，初始值为0
    observation = env.reset() # 重置游戏环境，开始新回合
    while True: # 不断循环，直到回合结束
        if render: # 判断是否显示
            env.render() # 显示图形界面
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action) # 执行动作
        episode_reward += reward # 收集回合奖励
        if train: # 判断是否训练智能体
            agent.learn(observation, action, reward, done) # 学习
        if done: # 回合结束，跳出循环
            break
        observation = next_observation
        # print('observaton:',observation)
    return episode_reward # 返回回合总奖励

env = gym.make('MountainCar-v0') # 创建一个小车爬山的环境
# print('观测空间 = {}'.format(env.observation_space))
# print('动作空间 = {}'.format(env.action_space))
# print('观测范围 = {} ~ {}'.format(env.observation_space.low,
#         env.observation_space.high))
# print('动作数 = {}'.format(env.action_space.n))
agent = SimpleAgent(env)
env.seed(3) # 设置随机种子，让结果可复现
episode_reward = play(env, agent, render=True)
print('回合奖励 = {}'.format(episode_reward))
env.close() # 关闭图形界面
