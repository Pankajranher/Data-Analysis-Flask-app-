import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import get_chart_data

main = Blueprint("main", __name__)

UPLOAD_FOLDER = "uploads"


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        return redirect(url_for("main.dashboard", filename=file.filename))


@main.route("/dashboard/<filename>")
def dashboard(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    df = pd.read_csv(filepath)

    # 🔹 Basic Cleaning
    df.dropna(inplace=True)

    # 🔹 Insights
    total_revenue = df["Revenue"].sum()
    top_product = df.groupby("Product")["Revenue"].sum().idxmax()

    # 🔹 Chart (Matplotlib)
    plt.figure()
    df.groupby("Product")["Revenue"].sum().plot(kind="bar")
    chart_path = os.path.join("static", "chart.png")
    plt.savefig(chart_path)
    plt.close()

    return render_template(
        "dashboard.html",
        revenue=total_revenue,
        top_product=top_product,
        chart=chart_path,
    )
