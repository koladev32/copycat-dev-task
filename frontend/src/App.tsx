import React, {useState} from 'react';
import * as Yup from "yup";
import {useFormik} from "formik";
import axios from "axios";
import Result from "./components/Result";

function App() {
    const [loading, setLoading] = useState(false)
    const [results, setResults] = useState([]);
    const handleParseAction = (html: string) => {
        axios.post(`${process.env.REACT_APP_API_URL}/parse_html/`, {html: String(html)}, {
            headers: {"content-Type": "text/plain"}
        })
            .then((res) => {
                setResults(res.data.data)
            }).catch((err) => {
            console.error(err)
        })

    }

    const formik = useFormik({
        initialValues: {
            html: ""
        },

        onSubmit: values => {
            setLoading(true);
            handleParseAction(values.html);
            setLoading(false);
        },
        validationSchema: Yup.object({
            html: Yup.string().trim().required("This field can't be blank.")
        })
    })
    return (
        <div className="p-6 h-screen">
            <h1 className="text-2xl font-bold">Find similar Node</h1>

            <div className="w-full h-3/4 mt-5">
                <h3 className="font-bold">Paste HTML in textbox below</h3>
                <form className="h-3/4" onSubmit={formik.handleSubmit}>
                    <textarea
                        className="border-2 border-gray-900 h-full w-full bg-gray-50"
                        id="html"
                        name="html"
                        value={formik.values.html}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.html && <div className="text-red-500">{formik.errors.html}</div>}

                    <div className="flex justify-center items-center mt-6">
                        <button
                            type="submit"
                            disabled={loading}
                            className="p-2 w-32 border-2 border-gray-800 bg-yellow-400 text-black font-bold"
                        >
                            Process Code
                        </button>
                    </div>
                </form>
            </div>

            <div className="flex flex-wrap justify-center m-4 space-x-4">
                {results && results.map((result, index) => {
                    // @ts-ignore
                    return (<Result count={result.count} value={result.value} className={result.className} innerHTML={result.innerHTML} parent={result.parent} tag={result.tag}/>)
                })}
            </div>
        </div>
    );
}

export default App;
