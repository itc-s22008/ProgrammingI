class Score:
    def change_score(self, score):
        lbl = tk.Label(wnd, text = "score: ", fg = "black", width = 5 )
        lbl.place(x = 410, y = 20)

        
        lbl = tk.Label(wnd, text=str(score), bg = "white", fg = "black",
                        width = 3, relief = "solid", anchor = "w" )
        lbl.place(x = 460, y = 20)
        return change_score
