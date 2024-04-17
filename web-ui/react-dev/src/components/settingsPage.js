import React, {Fragment} from "react";
import {Card, Row, Col, Button, Popconfirm, notification} from "antd";

class SettingsPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {

        }

        this.buttonCss = {
            marginRight: '10px',
            height: '40px',
            width: '200px',
            fontFamily: "'Euclid', sans-serif",
            fontSize: '18px',
        }

        this.cardCss = {
            backgroundColor: '#F0F0F0',
            width: '95%',
            margin: '10px auto',
            fontFamily: "'Euclid', sans-serif"
        }
    }

    handleReloadUI = () => {
        window.location.reload();
    }

    render() {
        return (
            <Fragment>
                <Card style={{...this.cardCss}}>
                    <p style={{fontSize: '24px', margin: '0 0 10px'}}>Clean up</p>
                    <Button disabled type={"primary"} style={{...this.buttonCss}}>Clean tmp files</Button>
                    <Button disabled type={"primary"} style={{...this.buttonCss}}>Clean tmp files</Button>
                </Card>
                <Card style={this.cardCss}>
                    <p style={{fontSize: '24px', margin: '0 0 10px'}}>Reload</p>
                    <Popconfirm title={"Reload UI"} description={"Are you sure to reload UI?"} okText={"Yes"} cancelText={"NO"} onConfirm={this.handleReloadUI} onCancel={() => {}}>
                        <Button type={"primary"} style={{...this.buttonCss}}>Reload UI</Button>
                    </Popconfirm>

                    <Button disabled type={"primary"} style={{...this.buttonCss}}>Reload Backend</Button>
                </Card>
            </Fragment>



        )
    }
}

export default SettingsPage;