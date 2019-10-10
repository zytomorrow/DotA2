-- 玩家表
CREATE TABLE IF NOT EXISTS players (
    steamid VARCHAR PRIMARY KEY,
    communityvisibilitystate TINYINT,
    personaname VARCHAR,
    lastlogoff DATE,
    profileurl VARCHAR,
    avatar VARCHAR,
    avatarmedium VARCHAR,
    avatarfull VARCHAR,
    personastate TINYINT,
    win TINYINT,
    lose TINYINT
);

-- 比赛详情表
CREATE TABLE IF NOT EXISTS matches (
    match_id INT PRIMARY KEY,
    barracks_status_dire INT,
    barracks_status_radiant INT,
    chat VARCHAR,
    cluster VARCHAR,
    cosmetics VARCHAR,
    dire_score INT,
    dire_team_id INT,
    draft_timings INt,
    duration INt,
    engine INt,
    first_blood_time INT,
    game_mode INT,
    human_players INT,
    leagueid INT,
    lobby_type INT,
    match_seq_num INT,
    negative_votes INT,
    objectives INT,
    picks_bans INT,
    positive_votes INT,
    radiant_gold_adv INT,
    radiant_score INT,
    radiant_team_id INT,
    radiant_win TINYINT,
    radiant_xp_adv TINYINT,
    skill VARCHAR start_time INT,
    teamfights INT,
    tower_status_dire INT,
    tower_status_radiant INT,
    versions INT,
    patch INT,
    region INT 
);

-- 玩家资料可见性状态码对应表
CREATE TABLE IF NOT EXISTS communityvisibilitystate ( 
    id TINYINT PRIMARY KEY, 
    decription VARCHAR );

-- 初始化玩家资料可见性状态码对应表
INSERT OR IGNORE INTO communityvisibilitystate
VALUES
	( 1, "Private" ),
	( 2, "Friends only" ),
	( 3, "Friends of friends" ),
	( 4, "Users only" ),
	( 5, "Public" );

-- 玩家表现表
CREATE TABLE IF NOT EXISTS player_performce (
    id INT PRIMARY KEY,
    MATCH_ID INT,
    playerid INT,
    abandons TINYINT,
    ability_targets char,
    ability_upgrades_arr char,
    ability_uses char,
    account_id char,
    actions char,
    additional_units char,
    assists TINYINT,
    backpack_0 INT,
    backpack_1 INT,
    backpack_2 INT,
    buyback_log INT,
    camps_stacked INT,

);


-- 玩家全英雄使用情况
CREATE TABLE IF NOT EXISTS playerid_use_hero(
    id INT PRIMARY KEY,
    playerid INT,
    hero_id TINYINT,
    last_played INT,
    games INT,
    win INT,
    with_games INT,
    with_win INT,
    against_games INT,
    against_win INT
)