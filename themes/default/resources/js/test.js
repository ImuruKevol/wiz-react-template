window.addEventListener("load", () => {
    const App = () => {
        console.log("asdl;fjka;sdljas;dlj")
        return (
            <div>
                this is react test
            </div>
        );
    }

    console.log(React);
    ReactDOM.render(
        <App />,
        document.querySelector("#react-test"),
    );

})