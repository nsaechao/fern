//
//  TokenResponse.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct TokenResponse: Codable {

    enum CodingKeys: String, CodingKey {
        case accessToken
        case expiresIn
        case refreshToken
    }

    public let accessToken: String
    public let expiresIn: Int
    public let refreshToken: String?

}
