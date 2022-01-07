# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nvflare.private.fed.protos import federated_pb2 as nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2


class FederatedTrainingStub(object):
    """The global federated model interfaces"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
            "/fedlearn.FederatedTraining/Register",
            request_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientLogin.SerializeToString,
            response_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
        )
        self.Quit = channel.unary_unary(
            "/fedlearn.FederatedTraining/Quit",
            request_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientState.SerializeToString,
            response_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
        )
        self.GetTask = channel.unary_unary(
            "/fedlearn.FederatedTraining/GetTask",
            request_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientState.SerializeToString,
            response_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.CurrentTask.FromString,
        )
        self.SubmitUpdate = channel.unary_unary(
            "/fedlearn.FederatedTraining/SubmitUpdate",
            request_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.Contribution.SerializeToString,
            response_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
        )
        self.Heartbeat = channel.unary_unary(
            "/fedlearn.FederatedTraining/Heartbeat",
            request_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.Token.SerializeToString,
            response_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
        )
        self.AuxCommunicate = channel.unary_unary(
            "/fedlearn.FederatedTraining/AuxCommunicate",
            request_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.AuxMessage.SerializeToString,
            response_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.AuxReply.FromString,
        )


class FederatedTrainingServicer(object):
    """The global federated model interfaces"""

    def Register(self, request, context):
        """client registration, so that it will contribute to the training"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Quit(self, request, context):
        """client quiting the federated training"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTask(self, request, context):
        """server to client model sharing"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitUpdate(self, request, context):
        """client to server contribution submission"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Heartbeat(self, request, context):
        """client to server heartbeat keep live"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AuxCommunicate(self, request, context):
        """client to server aux channel communication"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FederatedTrainingServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Register": grpc.unary_unary_rpc_method_handler(
            servicer.Register,
            request_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientLogin.FromString,
            response_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.SerializeToString,
        ),
        "Quit": grpc.unary_unary_rpc_method_handler(
            servicer.Quit,
            request_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientState.FromString,
            response_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.SerializeToString,
        ),
        "GetTask": grpc.unary_unary_rpc_method_handler(
            servicer.GetTask,
            request_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientState.FromString,
            response_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.CurrentTask.SerializeToString,
        ),
        "SubmitUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitUpdate,
            request_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.Contribution.FromString,
            response_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.SerializeToString,
        ),
        "Heartbeat": grpc.unary_unary_rpc_method_handler(
            servicer.Heartbeat,
            request_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.Token.FromString,
            response_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.SerializeToString,
        ),
        "AuxCommunicate": grpc.unary_unary_rpc_method_handler(
            servicer.AuxCommunicate,
            request_deserializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.AuxMessage.FromString,
            response_serializer=nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.AuxReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("fedlearn.FederatedTraining", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FederatedTraining(object):
    """The global federated model interfaces"""

    @staticmethod
    def Register(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fedlearn.FederatedTraining/Register",
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientLogin.SerializeToString,
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Quit(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fedlearn.FederatedTraining/Quit",
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientState.SerializeToString,
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetTask(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fedlearn.FederatedTraining/GetTask",
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.ClientState.SerializeToString,
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.CurrentTask.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fedlearn.FederatedTraining/SubmitUpdate",
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.Contribution.SerializeToString,
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Heartbeat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fedlearn.FederatedTraining/Heartbeat",
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.Token.SerializeToString,
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.FederatedSummary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AuxCommunicate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fedlearn.FederatedTraining/AuxCommunicate",
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.AuxMessage.SerializeToString,
            nvflare_dot_private_dot_fed_dot_protos_dot_federated__pb2.AuxReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
