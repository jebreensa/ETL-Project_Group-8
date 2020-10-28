from flask import Flask, render_template, jsonify
import psycopg2


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# setup postgres connection
conn = psycopg2.connect("dbname='NBA_API' user='postgres' host='localhost' password='YOUR_PASSWORD_HERE'")

#set up cursor

cur = conn.cursor()

@app.route("/")
def Home():

    return (
        f"-------------------<br/>"
        f"How to Use this API:<br/>"
        f"Form a URL for the Player and Year you want to view in this format:<br/>"
        f"/api/v1.0/api/nba/YEAR/PLAYER NAME<br/>"
        f"----------------<br/>"
        f"----------------<br/>"
        f"----------------<br/>"
        f"EXAMPLE: <br/>"
        f"----------------<br/>"
        f"----------------<br/>"
        f" /api/v1.0/nba/2017/James Harden ----><br/>"
        f"----------------<br/>"
        f"  player_id: 201935, <br/>"
        f"   player_name: James Harden, <br/>"
            f"player_age: 27.0,<br/>"
            f"full_team_name: Houston Rockets,<br/>"
            f"is_active: true,<br/>"
            f"season_id: 2017,<br/>"
            f"gp: 81,<br/>"
            f"gs: 81,<br/>"
            f"min: 2947.0,<br/>"
            f"fgm: 674,<br/>"
            f"fga: 1533,<br/>"
            f"fg_pct: 0.44,<br/>"
            f"fg3m: 262.0,<br/>"
            f"fg3a: 756.0,<br/>"
            f"fg3_pct: 0.34700000000000003,<br/>"
            f"ftm: 746,<br/>"
            f"fta: 881,<br/>"
            f"ft_pct: 0.847,<br/>"
            f"oreb: 95.0,<br/>"
            f"dreb: 564.0,<br/>"
            f"reb: 659.0,<br/>"
            f"ast: 907,<br/>"
            f"stl: 121.0,<br/>"
            f"blk: 38.0,<br/>"
            f"tov: 464.0,<br/>"
            f"pf: 215,<br/>"
            f"pts: 2356,<br/>"
            f"salary: 26540100.0,<br/>"
            f"per: 31.4942399,<br/>"
            f"cpi_ave: 245.12,<br/>"
            f"register_value: 10961<br/>"
            f"player_evaluation: 3.2134847648760063<br/>"
            f"----------------<br/>"
            f"----------------<br/>"
            f"TERMS: <br/>"
            f"PER: Player efficiency rating, an estimation of a players overall performance <br/>"
            f"cpi_ave: Consumer price index for the year used in calculations <br/>"
            f"player_evaluation: Estimation of overpay/underpay, a value higher than zero represents a high salary relative to performance, and a value lower than zero represents a lower salary relative to performance. The further from zero, the more extreme."
    )

@app.route("/api/v1.0/nba/<year>/<player>")
def player(player, year):

    cur.execute("""SELECT * FROM nba_stats_salaries_double WHERE season_id = (%s) AND player_name = (%s)""", (year, player))
    rows = cur.fetchall()
    for row in rows:
        
        player_dict = {"player_id": row[0],
                        "player_name": row[1],
                        "player_age": row[2],
                        "full_team_name": row[3],
                        "is_active": row[4],
                        "season_id": row[5],
                        "gp": row[6],
                        "gs": row[7],
                        "min": row[8],
                        "fgm": row[9],
                        "fga": row[10],
                        "fg_pct": row[11],
                        "fg3m": row[12],
                        "fg3a": row[13],
                        "fg3_pct": row[14],
                        "ftm": row[15],
                        "fta": row[16],
                        "ft_pct": row[17],
                        "oreb": row[18],
                        "dreb": row[19],
                        "reb": row[20], 
                        "ast": row[21],
                        "stl": row[22],
                        "blk": row[23],
                        "tov": row[24],
                        "pf": row[25],
                        "pts": row[26],
                        "salary": row[27],
                        "per": row[28],
                        "cpi_ave": row[29],
                        "player_evaluation": row[31]}

    return jsonify(player_dict)


if __name__ == "__main__":
    app.run(debug=True)
