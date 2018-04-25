POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 0.00274       # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

ADD_BACKGROUND_MORT = True  # if background mortality should be added

PSA_ON = True      # if probabilistic sensitivity analysis is on

TRANS_RATE_MATRIX = [
    [0.00,   0.015114,       0.00,        0.00,   0.0175], #Well
    [0.00,       0.00,  0.0002687,      0.0016,        0], #Stroke
    [0.00,  0.0004624,       0.00,           0,   0.0175], #Post-Stroke
    [0.00,       0.00,       0.00,        0.00,      0.0], #Dead
    [0.00,       0.00,       0.00,        0.00,      0.0] #Background Death
]

TRANS_RATE_MATRIX_ANTICOAG = [
    [0.00,   0.015114,       0.00,        0.00, 0.018375], #Well
    [0.00,       0.00,  0.0002687,      0.0016,        0], #Stroke
    [0.00,  0.0003468,       0.00,           0, 0.018375], #Post-Stroke
    [0.00,       0.00,       0.00,        0.00,      0.0], #Dead
    [0.00,       0.00,       0.00,        0.00,      0.0] #Background Death
]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke
    0.9,  # post-stroke
    0,  # dead
    0 #also dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0,
    0
]

Anticoag_COST = 750

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 1736.8 / 100,000
