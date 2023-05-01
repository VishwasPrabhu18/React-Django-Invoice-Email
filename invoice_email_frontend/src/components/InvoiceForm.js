import React, { useEffect, useState } from "react";
import axios from "axios";
import { API_URL } from '../constants';
import InvoiceData from "./InvoiceData";
import "./style.scss";

const InvoiceForm = () => {

    const [emailField, setEmailField] = useState({
        name: '',
        toEmail: '',
        subject: '',
        content: '',
    });

    useEffect(() => {
        let invoiceDir = document.getElementById("contentVal");
        let data = InvoiceData();
        invoiceDir.innerHTML = data;
    });

    const handleInput = (event) => {
        setEmailField({...emailField, [event.target.name]: event.target.value});
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        // sending data to django
        axios.post(API_URL, emailField).then((res) => {
            alert("Email Send Successfully...");
            setEmailField({name: '', toEmail: '', subject: ''});
            document.getElementById("contentVal")
        }).catch((err) => {
            alert("Erro While Sending");
            console.log(err);
        });
    }

    return (
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-1">
            <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                    React + Django Invoice Email
                </h2>
            </div>

            <div className="sm:mx-auto w-5/6 mt-10">
                <form className="space-y-6" onSubmit={handleSubmit} method="POST">
                    <div>
                        <label htmlFor="name" className="label-style">
                            Your Name
                        </label>
                        <div className="mt-2">
                            <input onChange={handleInput} value={emailField.name} name="name" type="text" required className="input-style" />
                        </div>
                    </div>
                    <div>
                        <label htmlFor="toEmail" className="label-style">
                            Email address
                        </label>
                        <div className="mt-2">
                            <input onChange={handleInput} value={emailField.toEmail} name="toEmail" type="email" required className="input-style" />
                        </div>
                    </div>
                    <div>
                        <label htmlFor="subject" className="label-style">
                            Subject
                        </label>
                        <div className="mt-2">
                            <input onChange={handleInput} value={emailField.subject} name="subject" type="text" required className="input-style" />
                        </div>
                    </div>

                    <div>
                        <label htmlFor="subject" className="label-style">
                            Content
                        </label>
                        <div id="contentVal" className="p-6 border rounded-lg bg-gray-50 dark:bg-gray-900 flex justify-center">
                            
                        </div>
                    </div>

                    <div>
                        <button type="submit" className="button1"> Send Email </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default InvoiceForm;