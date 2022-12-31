from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
import sys

from Master_Safe_Folder_Lock import *
from Master_Safe_lock import *
from Master_Safe_unlock import *
from Master_Safe_Setup import *


def resource_path(relative_path):
    """ Get Absolute Path To Resource"""
    try:
        base_path = getattr(sys, '_MEIPASS', '.')+'/'
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_pass():
    f_stat = f_state_config()
    c_pass_root = ""
    if f_stat == "Online":
        c_pass_root = Pass_root2
    elif f_stat == "Offline":
        c_pass_root = Pass_root
    elif f_stat == "nil":
        return "nil"

    with open(c_pass_root, "r+") as f:
        pass0 = f.read()
    return pass0, c_pass_root


def pass_change():
    def pass_process():
        entered_pass = pc_ent1.get()
        n0_pass = pc_ent2.get()
        n1_pass = pc_ent3.get()
        c_pass = get_pass()
        if c_pass[0] != entered_pass:
            messagebox.showerror("Master_Safe", "Current Password Is Incorrect.")
        else:
            if n0_pass != n1_pass:
                messagebox.showwarning("Master_Safe", "New Passwords Does Not Match.")
            else:
                with open(c_pass[1], "w+") as f:
                    f.write(n0_pass)
                    messagebox.showinfo("Master_Safe", "You Successfully Changed The Password To\n[{0}]".format(n0_pass))
                    p_c_window.destroy()

    p_c_window = Tk()
    p_c_window.geometry("350x250+70+70")
    p_c_window.resizable(False, False)
    p_c_window.title("New Password")
    pc_lbl1 = Label(p_c_window, text="Give your current password", bg="#4C4C4C", fg="#000000",
                    font=("helvetica", 14, "italic bold")).pack(fill="both")
    pc_ent1 = Entry(p_c_window, width=15, bg="#8E8E8E", font=("calligraphy", 13, "italic"))
    pc_ent1.pack(after=pc_lbl1, fill="both", ipady=5)
    pc_lbl2 = Label(p_c_window, text="Enter your new password", bg="#4C4C4C", fg="#000000",
                    font=("helvetica", 14, "bold italic")).pack(after=pc_ent1, fill="both")
    pc_ent2 = Entry(p_c_window, width=15, bg="#8E8E8E", font=("calligraphy", 13, "italic"))
    pc_ent2.pack(after=pc_lbl2, fill="both", ipady=5)
    pc_lbl3 = Label(p_c_window, text="Re-enter your new password", bg="#4C4C4C", fg="#000000",
                    font=("helvetica", 14, "bold italic")).pack(after=pc_ent2, fill="both")
    pc_ent3 = Entry(p_c_window, width=15, bg="#8E8E8E", font=("calligraphy", 13, "italic"))
    pc_ent3.pack(after=pc_lbl3, fill="both", ipady=5)

    pc_frm = Frame(p_c_window, bg="#4C4C4C")
    pc_frm.pack(fill="both")
    pc_btn1 = Button(pc_frm, text="Submit", bg="#4C4C4C", relief="raised", borderwidth=3, width=10,
                     font=("Ariel", 12, "bold"), command=pass_process)
    pc_btn1.pack(pady=20, padx=10)

    p_c_window.mainloop()


def req_pass(mode=0, window=None):
    def check_pass():
        pass1 = pass_ent.get()
        f_stat = f_state_config()
        c_pass_root = ""
        if f_stat == "Online":
            c_pass_root = Pass_root2
        elif f_stat == "Offline":
            c_pass_root = Pass_root
        elif f_stat == "nil":
            pass_lbl2.config(text="Program Unconfigured. Configure First.")

        with open(c_pass_root, "r+") as f:
            pass0 = f.read()
        if pass1 != pass0:
            pass_lbl2.config(text="Incorrect Password! Try Again")
            # pass_ent.config()
        elif pass1 == pass0:
            if mode == 0:
                folder_unlock()
            elif mode == 1:
                clear()
                window.destroy()

            data_init()
            pass_window.destroy()

    def lbl2_con():
        pass_lbl2.config(text="")
        pass_window.after(2000, lbl2_con)

    pass_window = Tk()
    pass_window.geometry("300x150+100+400")
    pass_window.resizable(False, False)
    pass_window.title("Master_Safe")
    pass_lbl = Label(pass_window, text="Enter Your Password :> ", bg="#4C4C4C", fg="#EEEEEE",
                     font=("italic", 12, "bold"))
    pass_lbl.pack(fill="both", pady=5, padx=5)
    pass_ent = Entry(pass_window, bg="#4C4C4C", width=20,
                     font=("calligraphy", 12, "italic"))
    pass_ent.pack(after=pass_lbl, fill="both", pady=5, padx=5)

    pass_lbl2 = Label(pass_window, text="", fg="red",
                      font=("Ariel", 9, "italic"))
    pass_lbl2.pack(after=pass_ent, fill="x", padx=5)
    pass_btn = Button(pass_window, text="OK", width=10, height=2, bg="#4C4C4C", fg="#EEEEEE",
                      anchor="c", command=check_pass)
    pass_btn.pack(after=pass_lbl2, fill="y", padx=5, pady=5)

    pass_window.after(0, lbl2_con)
    pass_window.mainloop()


def get_single():
    filename = filedialog.askopenfilename(initialdir=Clone_root, title="Select A File To Open")
    return filename


def f_state_config():
    if os.path.exists("SAFE"):
        return "Online"
    elif os.path.exists("MS_hidden-00978687##afd"):
        return "Offline"
    else:
        return "nil"


def f_state_gui_config():
    f_stat = f_state_config()
    if f_stat == "Online":
        f_btn.config(image=image2)
        f_stat_lbl.config(text="Online", fg="#1AC80F", font=("helvetica", 25, "bold italic"))
    elif f_stat == "Offline":
        f_btn.config(image=image1)
        f_stat_lbl.config(text="Offline", fg="#D20708", font=("helvetica", 25, "bold italic"))
    elif f_stat == "nil":
        f_btn.config(image=image4)
        f_stat_lbl.config(text='Unconfigured', fg="#5E9CFF", font=("helvetica", 21, "bold italic"))


def inf_state_gui_config(info):
    os.chdir(Main_root)
    f_stat = f_state_config()
    if f_stat == "Offline":
        info_new = info.format(t="***", c="***", f="***")
        info_pan.config(text=info_new)
    elif f_stat == "Online":
        clones, files = 0, 0
        for _ in clone_locate(Clone_root, 1):
            if os.path.isdir(_): continue
            clones += 1
        for _ in locate_files(Safe_root, 1):
            if os.path.isdir(_): continue
            files += 1
        info_new = info.format(t=clones + files, c=clones, f=files)
        info_pan.config(text=info_new)
    elif f_stat == "nil":
        info_pan.config(text="Program\n is\n not\n configured.")
    os.chdir(Main_root)


def data_init():
    f_state_gui_config()
    inf_state_gui_config(info_base)


def clear():
    f_stat = f_state_config()
    if f_stat == "Online":
        rmtree(Safe_root)
    elif f_stat == "Offline":
        os.system("icacls {0} /grant {1}:(F)".format(Hidden_root, os.environ["username"]))
        rmtree(Hidden_root)
    elif f_stat == "nil":
        messagebox.showerror("Master_Safe", "Program is not configured")


def p():
    f_stat = f_state_config()
    if f_stat == "Online":
        folder_lock()
        print("You Locked the Folder")
    elif f_stat == "Offline":
        req_pass(mode=0)
        print("You Unlocked the folder")
    elif f_stat == "nil":
        setup()
        messagebox.showinfo("Master_Safe", "You successfully configured the program\nYour Default Password is [ERROR401]")
    data_init()


def q():
    f_stat = f_state_config()
    if f_stat == "Online":
        lock(Safe_root)
    elif f_stat == "Offline":
        messagebox.showwarning("Master_Safe", "[SAFE] folder is Offline")
    elif f_stat == "nil":
        messagebox.showerror("Master_Safe", "Program is not Configured")
    data_init()


def r():
    f_stat = f_state_config()
    if f_stat == "Online":
        file = get_single()
        unlock_single(os.path.abspath(file))
    elif f_stat == "Offline":
        messagebox.showwarning("Master_Safe", "[SAFE] folder is Offline")
    elif f_stat == "nil":
        messagebox.showerror("Master_Safe", "Program is not Configured")
    data_init()


def s():
    f_stat = f_state_config()
    if f_stat == "Online":
        unlock(Clone_root)
        os.chdir(Main_root)
    elif f_stat == "Offline":
        messagebox.showwarning("Master_Safe", "[SAFE] folder is Offline")
    elif f_stat == "nil":
        messagebox.showerror("Master_Safe", "Program is not Configured")
    data_init()


def t():
    def nback():
        set_window.destroy()

    set_window = Tk()
    set_window.title("Settings")
    image5 = PhotoImage(master=set_window, file=resource_path('pass_change1.png'))
    image6 = PhotoImage(master=set_window, file=resource_path('Delete1.png'))
    set_window.geometry("+900+280")
    set_window.resizable(False, False)
    set_frm1 = Frame(set_window, bg="#4C4C4C")
    set_frm1.pack(fill="both")
    set_but1 = Button(set_frm1, relief="solid", image=image5, command=pass_change)
    set_but2 = Button(set_frm1, relief="solid", image=image6, command=partial(req_pass, mode=1, window=set_window))
    set_but1.pack(side="left", padx=20, pady=25)
    set_but2.pack(after=set_but1, side="left", padx=20, pady=25)
    set_frm2 = Frame(set_window, bg="#4C4C4C")
    set_frm2.pack(fill="both")
    set_btn_b = Button(set_frm2, text=" < BACK < ", anchor="c", relief="raised", borderwidth=3,
                       bg="#4C4C4C", fg="#000000", font=("Ariel", 10, "bold"), command=nback)
    set_btn_b.pack(side="bottom", padx=10, pady=30)

    set_window.mainloop()


f_status = "Offline"
info_base = """Total Files : {t}
Locked Files : {c}
Unlocked Files : {f}"""
Main_root = os.getcwd()
Safe_root = Main_root + "\\SAFE"
Hidden_root = Main_root + "\\MS_hidden-00978687##afd"
Pass_root = Main_root + "\\MS_hidden-00978687##afd\\.data\\.pass.MS"
Pass_root2 = Main_root + "\\SAFE\\.data\\.pass.MS"
Clone_root = Main_root + "\\SAFE\\.data\\.clone_tree"

root = Tk()
root.geometry("400x400+450+170")
root.resizable(False, False)
root.title("Master_Safe")

image1 = PhotoImage(file=resource_path('lock1.png'))
image2 = PhotoImage(file=resource_path('Unlock1.png'))
image3 = PhotoImage(file=resource_path('Settings1.png'))
image4 = PhotoImage(file=resource_path('New_Folder1.png'))

f1 = Frame(root, bg="#4C4C4C")
f2 = Frame(root, bg="#4C4C4C")
f3 = Frame(root, bg="#4C4C4C")
f1.pack(fill="x")
f2.pack(fill="x")
f3.pack(fill="both")

# Frame 1 Widgets
title = Label(f1, anchor="center", text="Master Safe - V2.0", font=("Ariel Black", 34), bg="#4C4C4C", fg="#EEEEEE")
title.pack(padx=5, pady=25)

# Frame 2 Widgets
f_stat_lbl = Label(f2, text=f_status, bg="#4C4C4C", font=("helvetica", 25, "bold italic"))
f_stat_lbl.pack(side="left", padx=60, pady=30)

f_btn = Button(f2, relief="raised", image=image1, bd=4, bg="black", command=p)
f_btn.pack(side="left", anchor="w", padx=10, pady=30)
sett_but = Button(f2, relief="raised", bd=4, bg="#000000", image=image3, command=t)
sett_but.pack(after=f_btn, padx=10, pady=30)

# Frame 3 Widgets
info_pan = Label(f3, font=("cosmic sans ms", 14, "italic"), relief="sunken", bg="#8E8E8E", height=60,
                 width=15)
info_pan.pack(anchor="w", side="left", padx=20, pady=10, ipadx=2)

frm_3_1 = Frame(f3, bg="#5C2E2E", relief="groove", borderwidth=4)
frm_3_1.pack(side="left", fill="both", padx=20, pady=10)
btn_1 = Button(frm_3_1, text="Lock All", bg="#797979", fg="#000000", font=("ariel", 10, "italic bold"), width=15,
               height=2, command=q)
btn_2 = Button(frm_3_1, text="Unlock One", bg="#797979", fg="#000000", font=("ariel", 10, "italic bold"), width=15,
               height=2, command=r)
btn_3 = Button(frm_3_1, text="Unlock All", bg="#797979", fg="#000000", font=("ariel", 10, "italic bold"), width=15,
               height=2, command=s)
btn_1.pack(pady=3, padx=20)
btn_2.pack(after=btn_1, pady=3, padx=20)
btn_3.pack(after=btn_2, pady=3, padx=20)

data_init()
root.mainloop()
