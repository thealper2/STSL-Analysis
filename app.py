import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

def matchcount(teamname):
    return len(df[df["home"] == teamname]) + len(df[df["visitor"] == teamname])

def query_long(teamname, target1, target2, year):
    tempdf_home = df[df["home"] == teamname]
    tempdf_visitor = df[df["visitor"] == teamname]
    home_target = target1
    visitor_target = target2

    home_target_match = None
    home_target_match_count = 0
    visitor_target_match = None
    visitor_target_match_count = 0


    for index, row in tempdf_home[tempdf_home["Season"] == year].iterrows():
        home_target_count = row[home_target]

        if home_target_count >= home_target_match_count:
            home_target_match_count = home_target_count
            home_target_match = row

    for index, row in tempdf_visitor[tempdf_visitor["Season"] == year].iterrows():
        visitor_target_count = row[visitor_target]

        if visitor_target_count >= visitor_target_match_count:
            visitor_target_match_count = visitor_target_count
            visitor_target_match = row

    result = None
    if home_target_match[target1] == None and visitor_target_match[target2] != None:
        result = visitor_target_match

    elif home_target_match[target1] != None and visitor_target_match[target2] == None:
        result = home_target_match

    elif home_target_match[target1] >= visitor_target_match[target2]:
        result = home_target_match

    else:
        result = visitor_target_match

    return result

def toplam_ve_kaybedilen_puan(teamname):
    # Takımın toplam kazandığı puanı hesapla
    toplam_puan = 0
    kaybedilen_puan = 0
    toplam_atilan_gol = 0
    toplam_yenilen_gol = 0
    ilk_yari_atilan_gol = 0
    ilk_yari_yenilen_gol = 0
    ikinci_yari_atilan_gol = 0
    ikinci_yari_yenilen_gol = 0
    ic_saha_kazanilan_mac_sayisi = 0
    ic_saha_kaybedilen_mac_sayisi = 0
    ic_saha_beraberlik_mac_sayisi = 0
    deplasman_kazanilan_mac_sayisi = 0
    deplasman_kaybedilen_mac_sayisi = 0
    deplasman_beraberlik_mac_sayisi = 0
    tempdf_home = df[df["home"] == teamname]
    tempdf_visitor = df[df["visitor"] == teamname]


    for index, row in tempdf_home.iterrows():
        if row["hgoal"] > row["vgoal"]:
            toplam_puan += 3
            toplam_atilan_gol += row["hgoal"]
            toplam_yenilen_gol += row["vgoal"]
            ilk_yari_atilan_gol += row["hgoal_half"]
            ilk_yari_yenilen_gol += row["vgoal_half"]
            ikinci_yari_atilan_gol += row["hgoal"] - row["hgoal_half"]
            ikinci_yari_yenilen_gol += row["vgoal"] - row["vgoal_half"]
            ic_saha_kazanilan_mac_sayisi += 1
        elif row["hgoal"] == row["vgoal"]:
            toplam_puan += 1
            kaybedilen_puan += 2
            toplam_atilan_gol += row["hgoal"]
            toplam_yenilen_gol += row["vgoal"]
            ilk_yari_atilan_gol += row["hgoal_half"]
            ilk_yari_yenilen_gol += row["vgoal_half"]
            ikinci_yari_atilan_gol += row["hgoal"] - row["hgoal_half"]
            ikinci_yari_yenilen_gol += row["vgoal"] - row["vgoal_half"]
            ic_saha_beraberlik_mac_sayisi += 1
        else:
            kaybedilen_puan += 3
            toplam_atilan_gol += row["hgoal"]
            toplam_yenilen_gol += row["vgoal"]
            ilk_yari_atilan_gol += row["hgoal_half"]
            ilk_yari_yenilen_gol += row["vgoal_half"]
            ikinci_yari_atilan_gol += row["hgoal"] - row["hgoal_half"]
            ikinci_yari_yenilen_gol += row["vgoal"] - row["vgoal_half"]
            ic_saha_kaybedilen_mac_sayisi += 1

    for index, row in tempdf_visitor.iterrows():
        if row["vgoal"] > row["hgoal"]:
            toplam_puan += 3
            toplam_atilan_gol += row["vgoal"]
            toplam_yenilen_gol += row["hgoal"]
            ilk_yari_atilan_gol += row["vgoal_half"]
            ilk_yari_yenilen_gol += row["hgoal_half"]
            ikinci_yari_atilan_gol += row["vgoal"] - row["vgoal_half"]
            ikinci_yari_yenilen_gol += row["hgoal"] - row["hgoal_half"]
            deplasman_kazanilan_mac_sayisi += 1
        elif row["vgoal"] == row["hgoal"]:
            toplam_puan += 1
            kaybedilen_puan += 2
            toplam_atilan_gol += row["vgoal"]
            toplam_yenilen_gol += row["hgoal"]
            ilk_yari_atilan_gol += row["vgoal_half"]
            ilk_yari_yenilen_gol += row["hgoal_half"]
            ikinci_yari_atilan_gol += row["vgoal"] - row["vgoal_half"]
            ikinci_yari_yenilen_gol += row["hgoal"] - row["hgoal_half"]
            deplasman_beraberlik_mac_sayisi += 1
        else:
            kaybedilen_puan += 3
            toplam_atilan_gol += row["vgoal"]
            toplam_yenilen_gol += row["hgoal"]
            ilk_yari_atilan_gol += row["vgoal_half"]
            ilk_yari_yenilen_gol += row["hgoal_half"]
            ikinci_yari_atilan_gol += row["vgoal"] - row["vgoal_half"]
            ikinci_yari_yenilen_gol += row["hgoal"] - row["hgoal_half"]
            deplasman_kaybedilen_mac_sayisi += 1

    return toplam_puan, kaybedilen_puan, toplam_atilan_gol, toplam_yenilen_gol, ilk_yari_atilan_gol, ilk_yari_yenilen_gol, ikinci_yari_atilan_gol, ikinci_yari_yenilen_gol, ic_saha_kazanilan_mac_sayisi, ic_saha_kaybedilen_mac_sayisi, ic_saha_beraberlik_mac_sayisi, deplasman_kazanilan_mac_sayisi, deplasman_kaybedilen_mac_sayisi, deplasman_beraberlik_mac_sayisi

def geriden_gelerek_kazanilan(teamname, year):
    tempdf_home = df[df["home"] == teamname]
    tempdf_visitor = df[df["visitor"] == teamname]

    tempdf_ggk = pd.DataFrame(columns=tempdf_home.columns)

    i = 0

    for index, row in tempdf_home.iterrows():
        if row["Season"] == year:
            if row["hgoal_half"] <= row["vgoal_half"]:
                if row["hgoal"] > row["vgoal"]:
                    tempdf_ggk.loc[i] = row
                    i+=1

    for index, row in tempdf_visitor.iterrows():
        if row["Season"] == year:
            if row["vgoal_half"] <= row["hgoal_half"]:
                if row["vgoal"] > row["hgoal"]:
                    tempdf_ggk.loc[i] = row
                    i+=1

    return tempdf_ggk

def derbiler(teamname, year):
    buyukler = ["Galatasaray", "Fenerbahce", "Besiktas", "Trabzonspor"]
    tempdf_home = df[df["home"] == teamname]
    tempdf_visitor = df[df["visitor"] == teamname]
    for i in range(4):
        if buyukler[i] == teamname:
            buyukler.pop(i)
        break

    derbidf_home = tempdf_home[(tempdf_home["visitor"] == buyukler[0]) | (tempdf_home["visitor"] == buyukler[1]) | (tempdf_home["visitor"] == buyukler[2])]
    derbidf_visitor = tempdf_visitor[(tempdf_visitor["home"] == buyukler[0]) | (tempdf_visitor["home"] == buyukler[1]) | (tempdf_visitor["home"] == buyukler[2])]
    tempdf_derbi = pd.DataFrame(columns=tempdf_home.columns)

    i = 0

    for index, row in derbidf_home.iterrows():
        if row["Season"] == year:
            tempdf_derbi.loc[i] = row
            i+=1

    for index, row in derbidf_visitor.iterrows():
        if row["Season"] == year:
            tempdf_derbi.loc[i] = row
            i+=1

    return tempdf_derbi

def sezon_gol(teamname, year):
    goal_home = 0
    goal_visitor = 0
    tempdf_home = df[df["home"] == teamname]
    tempdf_visitor = df[df["visitor"] == teamname]

    for index, row in tempdf_home[tempdf_home["Season"] == year].iterrows():
        goal_home += row["hgoal"]

    for index, row in tempdf_visitor[tempdf_visitor["Season"] == year].iterrows():
        goal_visitor += row["vgoal"]

    season_goal = goal_home + goal_visitor
    return season_goal

def derbi_sonuclari(teamname, date):
    derbi = derbiler(teamname, date)
    home_win = len(derbi[(derbi["home"] == teamname) & (derbi["hgoal"] > derbi["vgoal"])])
    home_loss = len(derbi[(derbi["home"] == teamname) & (derbi["hgoal"] < derbi["vgoal"])])
    home_draw = len(derbi[(derbi["home"] == teamname) & (derbi["hgoal"] == derbi["vgoal"])])
    visitor_win = len(derbi[(derbi["visitor"] == teamname) & (derbi["vgoal"] > derbi["hgoal"])])
    visitor_loss = len(derbi[(derbi["visitor"] == teamname) & (derbi["vgoal"] < derbi["hgoal"])])
    visitor_draw = len(derbi[(derbi["visitor"] == teamname) & (derbi["vgoal"] == derbi["hgoal"])])
    home_labels = ["", "", ""]
    home_y = [0, 0, 0]

    if home_win != 0 :
        home_y[0] += home_win
        home_labels[0] = "Kazandı"

    if visitor_win != 0:
        home_y[0] += visitor_win
        home_labels[0] = "Kazandı"

    if home_loss != 0:
        home_y[1] += home_loss
        home_labels[1] = "Kaybetti"

    if visitor_loss != 0:
        home_y[1] += visitor_loss
        home_labels[1] = "Kaybetti"

    if home_draw != 0 or visitor_draw != 0:
        home_y[2] += home_draw
        home_labels[2] = "Berabere"

    if visitor_draw != 0:
        home_y[2] += visitor_loss
        home_labels[2] = "Berabere"

    for i in range(len(home_labels)):
        if home_labels[i] == "":
            home_labels.pop(i)
        break

    for i in range(len(home_y)):
        if home_y[i] == 0:
            home_y.pop(i)
        break

    return home_y, home_labels

df = pd.read_csv("tsl_dataset.csv")
df = df[["Date", "Season", "Week", "home", "visitor", "FT", "hgoal", "vgoal", "hgoal_half", "vgoal_half", "HT", "fans", "home_red_card", "visitor_red_card"]]
teams = st.sidebar.selectbox("Takım", ("Galatasaray", "Fenerbahce", "Besiktas", "Trabzonspor"))
years = st.sidebar.selectbox("Yıl", list(dict.fromkeys(list(df["Season"].values))))

if st.sidebar.button("Analiz"):
    toplam_mac = matchcount(teams)
    toplam, kaybedilen, atilan, yenilen, ilk_yari_atilan, ilk_yari_yenilen, ikinci_yari_atilan, ikinci_yari_yenilen, icerde_kazanilan, icerde_kaybedilen, icerde_berabere, deplasmanda_kazanilan, deplasmanda_kaybedilen, deplasmanda_beraberlik = toplam_ve_kaybedilen_puan(teams)
    st.header("Genel İstatistikler")
    st.write("Oynanan toplam maç: ", str(toplam_mac))
    st.write("Toplam kazanılan puan: " + str(toplam))
    st.write("Toplam kaybedilen puan: " + str(kaybedilen))
    st.write("Toplam atılan gol: " + str(atilan))
    st.write("Toplam yenilen gol: " + str(yenilen))
    st.write("Toplam ilk yari atilan gol:", str(ilk_yari_atilan))
    st.write("Toplam ilk yari yenilen gol:", str(ilk_yari_yenilen))
    st.write("Toplam ikinci yari atilan gol:", str(ikinci_yari_atilan))
    st.write("Toplam ikinci yari yenilen gol:", str(ikinci_yari_yenilen))
    st.write("Evinde kazanilan mac sayisi:", str(icerde_kazanilan))
    st.write("Evinde kaybedilen mac sayisi:", str(icerde_kaybedilen))
    st.write("Evinde berabere biten mac sayisi:", str(icerde_berabere))
    st.write("Deplasmanda kazanilan mac sayisi:", str(deplasmanda_kazanilan))
    st.write("Deplasmanda kaybedilen mac sayisi:", str(deplasmanda_kaybedilen))
    st.write("Deplasmanda berabere biten mac sayisi:", str(deplasmanda_beraberlik))

    st.header("Sezon İstatistikleri")
    season_goal = sezon_gol(teams, years)
    st.write("Sezonda Atılan Gol Sayısı: " + str(season_goal))

    team_ggk = geriden_gelerek_kazanilan(teams, years)
    if team_ggk.empty == False:
        st.header("Geriden Gelerek Kazanilan Maclar")
        st.dataframe(team_ggk)

    home_most_red = query_long(teams, "home_red_card", "visitor_red_card", years)
    home_most_red = home_most_red.to_frame()
    if home_most_red.empty == False:
        st.header("En Çok Kırmızı Kart Gördüğü Maç")
        st.dataframe(home_most_red)

    visitor_most_red = query_long(teams, "visitor_red_card", "home_red_card", years)
    visitor_most_red = visitor_most_red.to_frame()
    if visitor_most_red.empty == False:
        st.header("Rakibinin En Çok Kırmızı Kart Gördüğü Maç")
        st.dataframe(visitor_most_red)


    derbys = derbiler(teams, years)
    st.header("Derbi Skorları")
    st.dataframe(derbys)

    st.header("Derbi Sonucları")
    derby_y, derby_labels = derbi_sonuclari(teams, years)
    fig, ax = plt.subplots()
    ax.pie(derby_y, labels=derby_labels, autopct="%1.1f%%")
    st.pyplot(fig)

    st.header(str(teams) + " takımının evinde atilan toplam goller")
    team_df_home = df[(df["Season"] == years) & (df["home"] == teams)]
    team_df_visitor = df[(df["Season"] == years) & (df["visitor"] == teams)]
    fig, ax = plt.subplots()
    sns.lineplot(x="visitor", y="hgoal", data=team_df_home, label="Atılan Goller")
    sns.lineplot(x="visitor", y="vgoal", data=team_df_home, label="Yenilen Goller")
    plt.xlabel("Rakipler")
    plt.ylabel("Gol Sayısı")
    plt.title(str(teams) + " takımının evindeki toplam goller")
    plt.legend()
    plt.xticks(rotation=90)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    st.header(str(teams) + " takımının deplasmanda atilan toplam goller")
    sns.lineplot(x="home", y="hgoal", data=team_df_visitor, label="Atılan Goller")
    sns.lineplot(x="home", y="vgoal", data=team_df_visitor, label="Yenilen Goller")
    plt.xlabel("Rakipler")
    plt.ylabel("Gol Sayısı")
    plt.title(str(teams) + " takımının deplasmandaki macları")
    plt.legend()
    plt.xticks(rotation=90)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    st.header(str(teams) + " takımının evindeki maçlarındaka çıkan kırmızı kartlar")
    sns.lineplot(x="visitor", y="home_red_card", data=team_df_home, label="Yenilen Kırmızı")
    sns.lineplot(x="visitor", y="visitor_red_card", data=team_df_home, label="Rakip Kırmızı")
    plt.xlabel("Rakipler")
    plt.ylabel("Kırmızı Kart Sayısı")
    plt.title(str(teams) + " takımının evindeki kırmızı kartlar")
    plt.legend()
    plt.xticks(rotation=90)
    st.pyplot(fig)


    fig, ax = plt.subplots()
    st.header(str(teams) + " takımının deplasmandaki maçlarında çıkan kırmızı kartlar")
    sns.lineplot(x="home", y="home_red_card", data=team_df_visitor, label="Yenilen Kırmızı")
    sns.lineplot(x="home", y="visitor_red_card", data=team_df_visitor, label="Rakip Kırmızı")
    plt.xlabel("Rakipler")
    plt.ylabel("Kırmızı Kart Sayısı")
    plt.title(str(teams) + " takımının deplasmandaki kırmızı kartlar")
    plt.legend()
    plt.xticks(rotation=90)
    st.pyplot(fig)
