import React from "react";
import { Row, Col } from "antd";

class Header extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            title: "Lstm-ar-stock-predict"
        };
    }

    render() {
        return (
            <div>
                <Row
                    style={{
                        height: "60px",
                        background: "linear-gradient(to bottom, #3300CC, #4775FF, #3300CC)",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center"
                    }}
                >
                    <Col
                        span={24}
                        style={{
                            paddingLeft: '24px',
                            fontSize: "36px",
                            fontFamily: "'Euclid', sans-serif",
                            color: "#FFFFFF",
                            textAlign: "left"
                        }}
                    >
                        {this.state.title}
                    </Col>
                </Row>
            </div>
        );
    }
}

export default Header;