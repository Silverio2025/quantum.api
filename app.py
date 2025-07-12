from flask import Flask, request, jsonify
from qiskit import QuantumCircuit
from qiskit_ibm_provider import IBMProvider
import os

app = Flask(__name__)

# Chave da IBM como variável de ambiente
provider = IBMProvider(token=os.environ.get("IBM_TOKEN"))

# Backend gratuito da IBM
backend = provider.get_backend("ibmq_qasm_simulator")

@app.route("/quantum", methods=["POST"])
def executar_qubit():
    data = request.json
    texto = data.get("texto", "")

    # Circuito quântico
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    job = backend.run(qc)
    result = job.result()
    counts = result.get_counts()

    return jsonify({
        "texto_recebido": texto,
        "resultado_qubit": counts
    })

app.run(host="0.0.0.0", port=8080)
