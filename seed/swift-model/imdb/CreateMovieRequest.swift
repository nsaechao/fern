//
//  CreateMovieRequest.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct CreateMovieRequest: Codable {

    enum CodingKeys: String, CodingKey {
        case title
        case rating
    }

    public let title: String
    public let rating: Double

}
