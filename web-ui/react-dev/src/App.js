import logo from './logo.svg';
import './App.css';
import Nav from "./components/nav";
import Header from "./components/header";
import GreedySearchChart from "./components/greedySearchChart";
import { Row, Col } from "antd";
import BeamSearchChart from "./components/beamSearchChart";
import SettingsPage from "./components/settingsPage"
import InformationPage from "./components/informationPage";
import React from "react";
import eventBus from "./components/eventBus";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            page: 'greedySearch',
        }
    }

    componentDidMount() {
        this.listenSwitchPage = eventBus.on('switch-page', this.handleSwitchPage);
    }

    componentWillUnmount() {
        this.listenSwitchPage.off();
    }

    handleSwitchPage = (toPage) => {
        this.setState({ page: toPage.to });
    }

    renderPage = () => {
        console.log(this.state.page)
        switch (this.state.page) {
            case 'greedySearch':
                return <GreedySearchChart></GreedySearchChart>;
            case 'beamSearch':
                return <BeamSearchChart></BeamSearchChart>;
            case 'settings':
                return <SettingsPage></SettingsPage>;
            case 'information':
                return <InformationPage></InformationPage>
            default:
                return <div>NULL</div>;
        }
    }

    render() {
        return (
            <div>
                <Header>ddd</Header>
                <Row>
                    <Col xxl={4} xl={5} lg={6} md={0} sm={0} xs={0}>
                        <Nav />
                    </Col>
                    <Col xxl={20} xl={19} lg={18} md={24} sm={24} xs={24}>
                        {this.renderPage()}

                    </Col>
                </Row>
            </div>
        );
    }
}

export default App;