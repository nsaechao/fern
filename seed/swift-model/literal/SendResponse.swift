//
//  SendResponse.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct SendResponse: Codable {

    enum CodingKeys: String, CodingKey {
        case message = "message"
        case status = "status"
        case success = "success"
    }

    public let message: String
    public let status: Int
    public let success: Bool

    public init(message: String, status: Int, success: Bool) {
        self.message = message
        self.status = status
        self.success = success
    }

}
